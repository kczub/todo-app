# Generated by Django 4.0.1 on 2022-01-25 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_todo_add_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='updated',
        ),
    ]