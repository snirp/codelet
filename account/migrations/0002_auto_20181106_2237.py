# Generated by Django 2.1.3 on 2018-11-06 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_auto_20181106_2201'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='correct',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cards.Choice'),
            preserve_default=False,
        ),
    ]
