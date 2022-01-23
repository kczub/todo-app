from django.db import models

class Todo(models.Model):
    content = models.TextField()

    def __str__(self) -> str:
        return self.content
