# Generated by Django 4.0.1 on 2022-02-24 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_postman_profile_pic_alter_postman_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='post',
        ),
    ]
