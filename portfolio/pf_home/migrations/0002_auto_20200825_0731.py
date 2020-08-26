# Generated by Django 2.1.5 on 2020-08-25 07:31

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('pf_home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmessage',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='clientmessage',
            name='message',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='clientmessage',
            name='name',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AlterField(
            model_name='clientmessage',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]