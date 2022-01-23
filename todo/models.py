from re import T
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    add_date = models.DateTimeField('date created', auto_now=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.title
