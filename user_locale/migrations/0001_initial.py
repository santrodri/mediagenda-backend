# Generated by Django 5.1.7 on 2025-03-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLocaleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CEP', models.CharField(max_length=9)),
                ('state', models.CharField(max_length=32)),
                ('locale', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('street', models.CharField(max_length=128)),
                ('number', models.CharField(max_length=8)),
            ],
        ),
    ]
