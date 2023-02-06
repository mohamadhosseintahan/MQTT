# Generated by Django 4.1.6 on 2023-02-06 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Log",
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
                ("DeviceID", models.CharField(max_length=200)),
                ("DeviceTime", models.DateTimeField()),
                ("Latitude", models.FloatField()),
                ("Longitude", models.FloatField()),
                ("Altitude", models.FloatField()),
                ("Course", models.FloatField()),
                ("Satellites", models.IntegerField()),
                ("SpeedOTG", models.FloatField()),
                ("AccelerationX1", models.FloatField()),
                ("AccelerationY1", models.FloatField()),
                ("Signal", models.IntegerField()),
                ("PowerSupply", models.IntegerField()),
            ],
        ),
    ]