from django.contrib import admin

# Register your models here.
from .models import SourceFormat, SourceURL, WeatherForecastCoast, SeaAreaForecastMet


admin.site.register(SourceFormat)
admin.site.register(SourceURL)
admin.site.register(WeatherForecastCoast)
admin.site.register(SeaAreaForecastMet)

