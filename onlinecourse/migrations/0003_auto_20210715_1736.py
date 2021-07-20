# Generated by Django 3.1.3 on 2021-07-15 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(default='', max_length=100)),
                ('is_correct', models.FloatField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='question',
            old_name='key',
            new_name='lesson',
        ),
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
        migrations.AddField(
            model_name='question',
            name='course',
            field=models.ManyToManyField(to='onlinecourse.Course'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.FloatField(default=0.0),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.ManyToManyField(to='onlinecourse.Choice')),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.enrollment')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ManyToManyField(to='onlinecourse.Question'),
        ),
    ]
