import os
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.contrib.auth import get_user_model
from ...models import Priority, State

class Command(BaseCommand):
    help = "Loads initial seed data."

    def handle(self, *args, **options):
        """
        Initial seed command. Handles seeding the database with certain predefined values and creating a
        base administrator account. This can only be executed if there is no other data/user loaded in the database.
        :param args:
        :param options:
        :return:
        """
        if Priority.objects.count() == 0:
            try:
                self.stdout.write("Writing seed data: Task Priorities", ending="\n")
                call_command('loaddata', os.path.join('todo','seed','0001_priorities.json'), app_label='todo')
            except Exception as ex:
                #Seed data was already loaded. Abort the install.
                self.stderr.write("Error: {}".format(ex), ending="\n")
                return
        else:
            self.stderr.write("Error: Priority data exists", ending="\n")

        if State.objects.count() == 0:
            try:
                self.stdout.write("Writing seed data: Task States", ending="\n")
                call_command('loaddata', os.path.join('todo','seed','0002_states.json'), app_label='todo')
            except:
                #Seed data was already loaded. Abort the install.
                self.stderr.write("Error: State data exists", ending="\n")
                return
        else:
            self.stderr.write("Error: State data exists", ending="\n")

        User = get_user_model()
        if User.objects.count() == 0:
            self.stdout.write("Creating admin user", ending="\n")
            self.stdout.write("Remember to change the default username/password!", ending="\n")
            User.objects.create_superuser(username="admin", password="admin", email="admin@example.com")
            self.stdout.write("Initial configuration completed.", ending="\n")
        else:
            self.stderr.write("Error: Other users exist. This command can only be run on"
                              " a clean install.", ending="\n")