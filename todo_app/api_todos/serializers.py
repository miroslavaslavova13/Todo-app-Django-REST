from rest_framework.serializers import ModelSerializer

from todo_app.api_todos.models import Todo, Category


class TodoForListSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title')


class TodoForCreateSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'category')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class TodoForDetailsSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'is_done')
