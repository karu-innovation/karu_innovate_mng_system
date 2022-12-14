# Generated by Django 4.1 on 2022-11-20 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('userview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userview', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Members',
                'db_table': 'members',
            },
        ),
    ]
