from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    future_date = models.DateTimeField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def valid_future_date(self):
        return self.future_date > timezone.now()

    def __str__(self) -> str:
        return self.title
