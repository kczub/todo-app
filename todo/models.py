from django.core.exceptions import ValidationError
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL

class Todo(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=30)
    content = models.TextField()
    future_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    # raises error in admin
    # def clean(self):
    #     if self.future_date < timezone.now().date():
    #         raise ValidationError("Date cannot be in the past.")

    def get_absolute_url(self):
        return reverse('todo:detail', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.title
