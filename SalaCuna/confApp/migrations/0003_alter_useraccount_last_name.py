# Generated by Django 4.2 on 2023-06-23 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confApp', '0002_rename_name_useraccount_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
