# Generated by Django 4.1 on 2023-01-23 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_topic_quiz_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.CharField(default='', max_length=150),
        ),
    ]
