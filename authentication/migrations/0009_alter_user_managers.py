# Generated by Django 4.2.7 on 2023-12-05 01:07

import authentication.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_user_password'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', authentication.models.MyUserManager()),
            ],
        ),
    ]