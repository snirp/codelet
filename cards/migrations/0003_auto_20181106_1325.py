# Generated by Django 2.1.3 on 2018-11-06 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20181106_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_text',
            new_name='choice',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='question',
        ),
    ]
