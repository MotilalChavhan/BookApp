# Generated by Django 4.0.5 on 2022-10-10 11:11

import BookApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0014_alter_transaction_book_alter_transaction_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='member',
            field=models.ForeignKey(null=True, on_delete=models.SET(BookApp.models.get_sentinel_user), to='BookApp.member'),
        ),
    ]
