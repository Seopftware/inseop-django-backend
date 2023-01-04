# Generated by Django 4.1.4 on 2023-01-04 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_user_gender_remove_user_is_business_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AddField(
            model_name="user",
            name="is_business",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="nickname",
            field=models.CharField(default="", max_length=30),
        ),
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="user",
            name="profileIntroduce",
            field=models.TextField(default="", max_length=200),
        ),
        migrations.AddField(
            model_name="user",
            name="sns",
            field=models.CharField(default="", max_length=10),
        ),
    ]
