from django.db import models


# Create your models here.
class WeatherForecastCoast(models.Model):
    area = models.CharField(max_length=300)
    wind = models.CharField(max_length=300)
    weather = models.TextField()
    visibility = models.CharField(max_length=300)
    sea_area_forecast_met = models.ForeignKey('SeaAreaForecastMet', on_delete=models.CASCADE)

    def __str__(self):
        return self.area

    class Meta:
        verbose_name_plural = 'weather forecast coasts'


class SeaAreaForecastMet(models.Model):
    title = models.CharField(max_length=200)
    until_time = models.CharField(max_length=250)
    issued_time = models.CharField(max_length=250)
    gale_status = models.CharField(max_length=10)
    small_craft_status = models.CharField(max_length=10)
    met_sit_head = models.TextField()
    met_sit_time = models.CharField(max_length=250)
    met_sit_text = models.TextField()
    outlook_time = models.CharField(max_length=250)
    outlook_head = models.TextField()
    outlook_text = models.TextField()
    swell_status = models.CharField(max_length=210)

    def __str__(self):
        return self.issued_time

    class Meta:
        verbose_name_plural = 'sea area forecasts met ie'


class SourceFormat(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'source formats'


class SourceURL(models.Model):
    name = models.CharField(max_length=25)
    url = models.CharField(max_length=250)
    description = models.CharField(max_length=250, blank=True, null=True)
    format = models.ForeignKey(SourceFormat, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'source urls'
