from django.contrib import admin

from . import models

admin.site.register(models.LogMessage)
admin.site.register(models.Booking)
admin.site.register(models.Film)
