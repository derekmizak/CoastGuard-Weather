from django.db import models

# Create your models here.

class WeatherRecord(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'weather records'


class SeaAreaForecastMetIe(models.Model):
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

    # Fields for coast data
    area1 = models.TextField(blank=True, null=True)
    wind1 = models.TextField(blank=True, null=True)
    weather1 = models.TextField(blank=True, null=True)
    visibility1 = models.TextField(blank=True, null=True)

    area2 = models.TextField(blank=True, null=True)
    wind2 = models.TextField(blank=True, null=True)
    weather2 = models.TextField(blank=True, null=True)
    visibility2 = models.TextField(blank=True, null=True)

    area3 = models.TextField(blank=True, null=True)
    wind3 = models.TextField(blank=True, null=True)
    weather3 = models.TextField(blank=True, null=True)
    visibility3 = models.TextField(blank=True, null=True)

    area4 = models.TextField(blank=True, null=True)
    wind4 = models.TextField(blank=True, null=True)
    weather4 = models.TextField(blank=True, null=True)
    visibility4 = models.TextField(blank=True, null=True)

    area5 = models.TextField(blank=True, null=True)
    wind5 = models.TextField(blank=True, null=True)
    weather5 = models.TextField(blank=True, null=True)
    visibility5 = models.TextField(blank=True, null=True)

    # Add more fields if you expect more coast elements

    def __str__(self):
        return f"{self.title}" - "{self.issued_time}"

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
