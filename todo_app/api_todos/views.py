from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView

from todo_app.api_todos.models import Todo, Category
from todo_app.api_todos.serializers import CategorySerializer, TodoForCreateSerializer, TodoForListSerializer, \
    TodoForDetailsSerializer


class ListCreateTodoApiView(ListCreateAPIView):
    queryset = Todo.objects.all()

    create_serializer_class = TodoForCreateSerializer
    list_serializer_class = TodoForListSerializer

    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class
        return self.create_serializer_class

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)
        category_id = self.request.query_params.get('category', None)

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset


class ListCategoryApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        return self.queryset.filter(todo__user_id=self.request.user.id).distinct()


class DetailsTodoApiView(RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoForDetailsSerializer

    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_object(self):
        todo = super().get_object()

        if todo.user != self.request.user:
            raise PermissionDenied

        return todo
