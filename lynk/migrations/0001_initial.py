# Generated by Django 4.2.2 on 2023-06-11 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("email_confirmed", models.BooleanField(default=False)),
                ("phone", models.CharField(max_length=200)),
                ("username", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="SocialAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instagram", models.CharField(max_length=250)),
                ("tiktok", models.CharField(max_length=250)),
                ("twitter", models.CharField(max_length=250)),
                ("linkedin", models.CharField(max_length=250)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="lynk.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Element",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item_type", models.CharField(max_length=50)),
                ("text_header", models.CharField(max_length=50)),
                ("yt_link", models.CharField(max_length=50)),
                ("web_link", models.CharField(max_length=50)),
                ("web_link_header", models.CharField(max_length=50)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="lynk.user"
                    ),
                ),
            ],
        ),
    ]
