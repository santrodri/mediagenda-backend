# Generated by Django 5.1.7 on 2025-03-24 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avatar', '0002_remove_avatarmodel_user_locale_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatarmodel',
            old_name='user',
            new_name='fk_user',
        ),
        migrations.RenameField(
            model_name='avatarmodel',
            old_name='user_locale',
            new_name='fk_user_locale',
        ),
    ]
