# Generated by Django 4.0.1 on 2022-01-27 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_todo_timestamp_todo_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
