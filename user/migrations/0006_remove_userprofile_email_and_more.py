# Generated by Django 4.2 on 2023-04-21 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userprofile_email_userprofile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone_number',
        ),
    ]
