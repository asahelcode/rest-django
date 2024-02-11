from .views import TodoList, TodoDetail
from django.urls import path

urlpatterns = [
  path("", TodoList.as_view(), name="todo_list"),
  path("<int:pk>/", TodoDetail.as_view(), name="todo_detail")
]