# Generated by Django 2.1.5 on 2019-12-17 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20191217_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
