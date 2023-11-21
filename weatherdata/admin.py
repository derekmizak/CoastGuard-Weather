from django.contrib import admin

# Register your models here.
from .models import WeatherData

admin.site.register(WeatherData)
