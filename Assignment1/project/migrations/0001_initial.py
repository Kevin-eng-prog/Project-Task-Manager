# Generated by Django 3.1.4 on 2020-12-14 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=200)),
                ('project_description', models.TextField()),
                ('project_duration', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('task_description', models.TextField()),
                ('task_start', models.DateField()),
                ('task_end', models.DateField()),
                ('project_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
    ]
