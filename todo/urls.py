from django.urls import path

from . import views

app_name = "todo"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("home", views.index_view, name="home"),
    path("task/list", views.TaskListView.as_view(), name="tasklist"),
    path("task/details/<int:id>", views.task_details_view, name="taskdetails"),
    path("task/delete/<int:id>", views.task_delete_view, name="taskdelete"),
    path("task/edit/<int:id>", views.task_edit_view, name="taskedit"),
    path("task/add", views.task_create_view, name="taskcreate"),
    path("logout", views.logout_view, name="logout"),
]