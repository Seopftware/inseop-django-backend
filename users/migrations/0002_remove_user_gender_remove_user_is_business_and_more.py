# Generated by Django 4.1.4 on 2023-01-04 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="gender",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_business",
        ),
        migrations.RemoveField(
            model_name="user",
            name="nickname",
        ),
        migrations.RemoveField(
            model_name="user",
            name="phone",
        ),
        migrations.RemoveField(
            model_name="user",
            name="profileIntroduce",
        ),
        migrations.RemoveField(
            model_name="user",
            name="sns",
        ),
    ]