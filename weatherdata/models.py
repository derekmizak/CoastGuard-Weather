from django.db import models

# Create your models here.

class WeatherRecord(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'weather records'


class SourceFormat(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'source formats'  

class SourceURL(models.Model):
    name = models.CharField(max_length=25)
    url = models.CharField(max_length=250)
    format = models.ForeignKey(SourceFormat, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'source urls'
