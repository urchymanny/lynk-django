# Generated by Django 4.2.2 on 2023-06-11 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lynk", "0005_alter_user_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="instagram",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name="user",
            name="linkedin",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name="user",
            name="tiktok",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name="user",
            name="twitter",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.DeleteModel(
            name="SocialAccount",
        ),
    ]
