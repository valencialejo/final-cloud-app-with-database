# Generated by Django 3.1.3 on 2021-07-20 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0005_choice_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]
