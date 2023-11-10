import datetime
from django.test import TestCase
from .models import Task
from .models import State
from .models import Priority
from django.contrib.auth import get_user_model
# Create your tests here.

class TaskTestCase(TestCase):
    def setUp(self):
        Priority(priority_name="Lowest").save()
        Priority(priority_name="Low").save()
        Priority(priority_name="Medium").save()
        Priority(priority_name="High").save()
        Priority(priority_name="Critical").save()

        State(state_name="Not Started").save()
        State(state_name="In Progress").save()
        State(state_name="Implemented").save()
        State(state_name="In Review").save()
        State(state_name="Completed").save()

        User = get_user_model()
        if User.objects.exists():
            return

        User.objects.create_superuser(username="admin", password="admin", email="admin@example.com")
        return

    def test_tasks(self):
        due_date = datetime.datetime(2023, 12, 19, 12, 00, 00)
        User = get_user_model()
        # Positive Test: Create a valid task
        try:
            task = Task(task_name="Test Task", task_owner=User.objects.get(username="admin"),
                    task_priority=Priority.objects.get(priority_name="Lowest"),
                    task_state=State.objects.get(state_name="Not Started"),
                    task_description="Test Task 1's Description",
                    task_due_date=due_date, tags="")

            # Full clean both checks input and validates
            task.full_clean()
            task.save()
        except:
            self.fail("Valid task was not written to database")

        self.assertTrue(task.pk is not None, "Valid task not written to database")

        task = None
        # Demonstrate that html data inside of fields is removed by fullclean
        try:
            task = Task(task_name="Test Task", task_owner=User.objects.get(username="admin"),
                    task_priority=Priority.objects.get(priority_name="Lowest"),
                    task_state=State.objects.get(state_name="Not Started"),
                    task_description="<script>alert();</script>",
                    task_due_date=due_date, tags="")

            # Full clean both checks input and validates
            task.full_clean()
            task.save()
        except:
            self.fail("Test 2: Valid task was not written to database")

        self.assertFalse( "<script>" not in task.task_description,
                            "Input was not cleaned correctly. <script> tag remained!")

        # Negative Test: Demonstrate that you cannot create an invalid task.
        task = None
        try:

            task = Task(task_name="Test Task", task_owner=None,
                    task_priority=Priority.objects.get(priority_name="Lowest"),
                    task_state=State.objects.get(state_name="Not Started"),
                    task_description="Test Task 1's Description",
                    task_due_date=due_date, tags="")

            # Full clean both checks input and validates
            task.full_clean()
            task.save()
        except:
            # We anticipate an exception here, which was thrown when validating/saving an invalid object
            pass
        self.assertFalse(task.pk is not None, "Invalid object written to database")  # Fails if invalid object written
