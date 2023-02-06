from django.contrib import admin

from mqtt.models import WarningLog, Log


@admin.register(Log)
class LogModelAdmin(admin.ModelAdmin):
    list_display = [
        "DeviceID",
        "DeviceTime",
        "Latitude",
        "Longitude",
        "Altitude",
        "Course",
        "Satellites",
        "SpeedOTG",
        "AccelerationX1",
        "AccelerationY1",
        "Signal",
        "PowerSupply",
    ]


@admin.register(WarningLog)
class WarningLogModelAdmin(admin.ModelAdmin):
    list_display = [
        "DeviceID",
        "WarningTime",
        "WarningType",
    ]
