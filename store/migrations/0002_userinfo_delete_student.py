# Generated by Django 4.2.3 on 2023-08-10 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserInfo",
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
                ("name", models.CharField(max_length=100)),
                ("dob", models.DateField()),
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=10)),
                ("phone_number", models.CharField(max_length=15)),
                ("mail_id", models.EmailField(max_length=254)),
                ("address", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="Student",
        ),
    ]
