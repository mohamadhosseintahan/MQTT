# Generated by Django 4.1.6 on 2023-02-06 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mqtt", "0002_warninglog"),
    ]

    operations = [
        migrations.CreateModel(
            name="CheckClient",
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
                ("active", models.BooleanField(editable=False)),
                ("client", models.CharField(editable=False, max_length=200)),
            ],
        ),
    ]
