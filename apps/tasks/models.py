from django.db import models
from ..users.models import User


class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField(blank = False)
    completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    helpers = models.ManyToManyField(User, related_name="colaborations")
