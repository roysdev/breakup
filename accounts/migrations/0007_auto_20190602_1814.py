# Generated by Django 2.1.7 on 2019-06-03 01:14

from django.db import migrations
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_userprofile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=smartfields.fields.ImageField(default=1, upload_to='avatar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar_jpeg',
            field=smartfields.fields.ImageField(default=1, upload_to='avatar'),
            preserve_default=False,
        ),
    ]
