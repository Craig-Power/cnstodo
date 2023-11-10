from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .forms import TaskForm
from .models import Task

@login_required(login_url="login")
def index_view(request):
    """
    Default route, redirects to login (or task list). Included for expansion with front page.
    :param request:
    :return:
    """
    return redirect('todo:tasklist')


def login_view(request):
    """
    Login view. Prompts user with login form, or redirects to task list if already logged in
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return redirect('todo:tasklist')
    else:
        return render(request=request, template_name="registration/login.html")

def logout_view(request):
    """
    Logout view. Destroys session, then returns to login page
    :param request:
    :return:
    """
    logout(request)
    messages.add_message(request, messages.SUCCESS, "You have successfully logged out")
    return redirect('login')

class TaskListView(ListView):
    """
    TaskList view. Provides logged in user with paginated list of tasks assigned to them.
    Clicking on a task opens details. Superusers can view all tasks.
    :param request:
    :return:
    """
    model = Task
    paginate_by = 10
    def get_queryset(self):
        filter = self.request.GET.get('filter', '')
        if(self.request.user.is_superuser):
            object_list = self.model.objects.filter(task_name__icontains=filter)
        else:
            object_list = self.model.objects.filter(task_owner=self.request.user,
                                                    task_name__icontains=filter)
        return object_list

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        return context

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.add_message(self.request, messages.ERROR, "You must be logged in to view this page.")
            return redirect('login')

        return super(TaskListView, self).get(*args, **kwargs)

@login_required(login_url="login")
def task_details_view(request, id=None):
    """
    Provides logged in user with details about a specific task, with option to edit or delete. Will redirect to task
    list if the user isn't a superuser or doesn't own tne task
    :param request:
    :return:
    """
    if id is None:
        return redirect('todo:tasklist')
    task=None

    try:
        task = Task.objects.get(pk=id)
    except Exception as ex:
        # The task doesn't exist. Bad request. Redirect back to the users task list.
        messages.add_message(request, messages.ERROR, "No such task found.")
        return redirect('todo:tasklist')

    if not request.user.is_superuser and not request.user.id == task.task_owner_id:
        messages.add_message(request, messages.ERROR, "An error occurred while opening this task.")
        return redirect('todo:tasklist')
    context = {"task":task}

    return render(request=request, template_name="todo/task_view.html", context=context)


@login_required(login_url="login")
def task_delete_view(request, id=None):
    """
    Allows logged in user to delete a task they own (or a superuser to delete any task). Returns to task list regardless
    of outcome.
    :param request:
    :param id:
    :return:
    """
    # Fix CSRF Vulnerability
    if request.method != 'POST':
        return redirect('todo:tasklist')

    if id is None:
        return redirect('todo:tasklist')

    try:
        task = Task.objects.get(pk=id)
    except:
        # The task likely doesn't exist. Bad URL maybe? Redirect back to the users task list.
        messages.add_message(request, messages.ERROR, "No such task found.")
        return redirect('todo:tasklist')

    # Does the user have permissions to delete the task?
    if not request.user.is_superuser and not request.user.id == task.task_owner_id:
        messages.add_message(request, messages.ERROR, "An error occurred while deleting this task.")
        return redirect('todo:tasklist')
    messages.add_message(request, messages.SUCCESS, "Task deleted successfully.")
    task.delete()

    # After all that, we're still redirecting to the same page.
    return redirect('todo:tasklist')

@login_required(login_url="login")
def task_edit_view(request, id=None):
    """
    Allows logged in user to edit a task they have access to (superuser or owner). On GET, presents a form with
    populated details. On POST, validates and updates the associated task.
    :param request:
    :param id:
    :return:
    """
    context = {}
    if id is None:
        return redirect('todo:tasklist')
    try:
        task = Task.objects.get(pk=id)
    except:
        # The task likely doesn't exist. Bad URL maybe? Redirect back to the users task list.
        return redirect('todo:tasklist')

    # Does the user have permissions to delete the task?
    if not request.user.is_superuser and not request.user.id == task.task_owner_id:
        return redirect('todo:tasklist')
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Task updated successfully.")
        return redirect("todo:taskdetails", id=task.pk)
    context['form'] = form
    context['task'] = task

    return render(request, "todo/task_edit.html", context)

@login_required(login_url="login")
def task_create_view(request):
    """
    Allows logged in user to create a new task that will automatically be assigned to them.
    :param request:
    :return:
    """
    context = {}
    if(request.method == 'POST'):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.task_owner = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS, "Task created successfully.")
            return redirect("todo:taskdetails", id=form.instance.pk)
    form = TaskForm()
    context['form'] = form
    return render(request, "todo/task_edit.html", context)