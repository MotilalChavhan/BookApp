# Generated by Django 4.0.5 on 2022-09-26 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0003_remove_book_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='issued_books',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookApp.book'),
        ),
    ]
