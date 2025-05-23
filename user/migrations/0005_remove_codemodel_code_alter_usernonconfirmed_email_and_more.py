# Generated by Django 5.1.7 on 2025-04-11 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_usernonconfirmed_rename_userd_codemodel_used_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codemodel',
            name='code',
        ),
        migrations.AlterField(
            model_name='usernonconfirmed',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='usernonconfirmed',
            name='username',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
