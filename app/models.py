from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(blank=True, null=True)

    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=MEDIUM)

    # File upload fields
    image = models.ImageField(upload_to='uploads/images/', blank=True, null=True)
    document = models.FileField(upload_to='uploads/documents/', blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    # ForeignKey to associate the comment with a todo item and user
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.todo.title}"