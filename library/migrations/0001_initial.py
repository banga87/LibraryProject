# Generated by Django 4.2.2 on 2023-06-15 06:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('is_borrowed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('return_date', models.DateTimeField(default=datetime.datetime(2023, 6, 29, 6, 54, 33, 291638, tzinfo=datetime.timezone.utc))),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_books', models.ManyToManyField(related_name='borrowed_books', through='library.Borrowing', to='library.book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='borrowing',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.student'),
        ),
    ]