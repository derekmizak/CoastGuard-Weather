from django.contrib import admin

# Register your models here.
from .models import SeaAreaForecastMetIe, SourceFormat, WeatherRecord, SourceURL

admin.site.register(SeaAreaForecastMetIe)
admin.site.register(SourceFormat)
admin.site.register(WeatherRecord)
admin.site.register(SourceURL)

