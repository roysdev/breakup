# Generated by Django 2.1.7 on 2019-06-01 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='text',
        ),
    ]