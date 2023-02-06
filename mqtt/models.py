from django.db import models


class Log(models.Model):
    DeviceID = models.CharField(max_length=200)
    DeviceTime = models.DateTimeField()
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.FloatField()
    Course = models.FloatField()
    Satellites = models.IntegerField()
    SpeedOTG = models.FloatField()
    AccelerationX1 = models.FloatField()
    AccelerationY1 = models.FloatField()
    Signal = models.IntegerField()
    PowerSupply = models.IntegerField()

    def __str__(self):
        return f"{self.DeviceID}"


class WarningLog(models.Model):
    
    DeviceID = models.CharField(max_length=200)
    WarningTime = models.DateTimeField()
    WarningType = models.IntegerField()

    def __str__(self):
        return f"{self.DeviceID}"

class CheckClient(models.Model):
    active = models.BooleanField(editable=False)
    client = models.CharField(max_length=200, editable=False, null=True, blank=True)

    def __str__(self):
        return f"{self.client} - {self.active}"