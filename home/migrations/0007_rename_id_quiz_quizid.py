# Generated by Django 4.1 on 2023-01-23 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_id_topic_topicid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='id',
            new_name='quizid',
        ),
    ]