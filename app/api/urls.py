from django.urls import path
from .views import TodoList, todo_detail, CommentList, comment_detail, UserList, user_detail

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('todos/', TodoList.as_view(), name='todo-list'),
    path('todos/<int:pk>/', todo_detail, name='todo-detail'),
    path('todos/<int:fk>/comments/', CommentList.as_view(), name='comment-list'),
    path('todos/<int:fk>/comments/<int:pk>/', comment_detail, name='comment-detail'),
]
