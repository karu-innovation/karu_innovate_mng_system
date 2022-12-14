# Generated by Django 4.1 on 2022-11-20 11:08

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
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cover_image', models.ImageField(upload_to='images/')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Communities',
                'db_table': 'community',
            },
        ),
    ]
