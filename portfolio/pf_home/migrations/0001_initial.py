# Generated by Django 2.1.5 on 2020-08-26 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=264)),
                ('code', models.CharField(blank=True, default='91', max_length=2)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
