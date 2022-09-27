# Generated by Django 4.0.5 on 2022-09-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0006_alter_user_issued_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='issued_books',
        ),
        migrations.AddField(
            model_name='user',
            name='issued_books',
            field=models.ManyToManyField(blank=True, null=True, to='BookApp.book'),
        ),
    ]
