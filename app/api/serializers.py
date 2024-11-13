from rest_framework import serializers
from app.models import User, Todo, Comment

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    title = serializers.CharField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    due_date = serializers.DateTimeField()
    status = serializers.ChoiceField(choices=Todo.STATUS_CHOICES)
    priority = serializers.ChoiceField(choices=Todo.PRIORITY_CHOICES)
    image = serializers.ImageField(required=False, allow_null=True)
    document = serializers.FileField(required=False, allow_null=True)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.status = validated_data.get('status', instance.status)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.image = validated_data.get('image', instance.image)
        instance.document = validated_data.get('document', instance.document)
        instance.save()
        return instance

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    todo = serializers.PrimaryKeyRelatedField(queryset=Todo.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.todo = validated_data.get('todo', instance.todo)
        instance.user = validated_data.get('user', instance.user)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance