# Generated by Django 4.1 on 2022-11-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountUsers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]