# Generated by Django 2.1.5 on 2020-08-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pf_home', '0003_auto_20200825_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmessage',
            name='code',
            field=models.CharField(blank=True, default='91', max_length=264),
        ),
        migrations.AlterField(
            model_name='clientmessage',
            name='phone',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]
