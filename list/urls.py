from django.urls import path

from list.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView, task_ready_or_not,
)

urlpatterns = [
    path(
        "",
        TaskListView.as_view(),
        name="task-list",
    ),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "task/<int:pk>/task-ready-or-not/",
        task_ready_or_not,
        name="task-ready-or-not",
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list",
    ),
    path(
        "tag/create/",
        TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tag/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tag/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
]

app_name = "todo_list"
