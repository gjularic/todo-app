from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):

    # delete tasks if user gets deleted
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # order tasks by 'complete' value
    # push completed items to the bottom
    class Meta:
        ordering = ['complete']