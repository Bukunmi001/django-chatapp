# Generated by Django 3.2.7 on 2022-09-13 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_todos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
