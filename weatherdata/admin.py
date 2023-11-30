from django.contrib import admin

# Register your models here.
from .models import SourceFormat, SourceURL, WeatherForecastCoast, SeaAreaForecastMet, MetOceanBuoyData, WeatherBuoy

class SeaAreaForecastMetAdmin(admin.ModelAdmin):
    list_display = ('issued_time', 'gale_status', 'small_craft_status', 'met_sit_head', 'met_sit_time', 'met_sit_text')
    search_fields = ('issued_time', 'gale_status', 'small_craft_status', 'met_sit_head', 'met_sit_time', 'met_sit_text')


class WeatherForecastCoastAdmin(admin.ModelAdmin):
    list_display = ('area', 'wind', 'weather', 'visibility', 'sea_area_forecast_met')
    search_fields = ('area', 'wind', 'weather', 'visibility', 'sea_area_forecast_met')

admin.site.register(SourceFormat)
admin.site.register(SourceURL)
admin.site.register(WeatherForecastCoast, WeatherForecastCoastAdmin)
admin.site.register(SeaAreaForecastMet, SeaAreaForecastMetAdmin)
admin.site.register(MetOceanBuoyData)
admin.site.register(WeatherBuoy)


