# Generated by Django 4.0.1 on 2022-02-18 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_todo_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='slug',
        ),
    ]
