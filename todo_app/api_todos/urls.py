from django.urls import path

from todo_app.api_todos.views import ListCreateTodoApiView, ListCategoryApiView, DetailsTodoApiView

urlpatterns = [
    path('', ListCreateTodoApiView.as_view(), name='api list todos'),
    path('categories/', ListCategoryApiView.as_view(), name='api list categories'),
    path('<int:pk>/', DetailsTodoApiView.as_view(), name='api details todo')
]