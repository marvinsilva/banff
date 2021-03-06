# Generated by Django 2.2.13 on 2020-07-16 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255, verbose_name='Course Title')),
                ('url', models.URLField(unique=True, verbose_name='Course URL')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255, verbose_name='Evaluator Name')),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('evaluation', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Evaluation Score')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Evaluations', to='courses.Course')),
            ],
            options={
                'verbose_name': 'Evaluation',
                'verbose_name_plural': 'Evaluations',
                'unique_together': {('email', 'course')},
            },
        ),
    ]
