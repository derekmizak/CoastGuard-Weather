from django.db import models


# Create your models here.
class WeatherForecastCoast(models.Model):
    area = models.CharField(max_length=600)
    wind = models.CharField(max_length=600)
    weather = models.TextField()
    visibility = models.CharField(max_length=600)
    sea_area_forecast_met = models.ForeignKey('SeaAreaForecastMet', on_delete=models.CASCADE)

    def __str__(self):
        return self.area

    class Meta:
        verbose_name_plural = 'weather forecast coasts'


class SeaAreaForecastMet(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    until_time = models.CharField(max_length=250, null=True, blank=True)
    issued_time = models.CharField(max_length=250, null=True, blank=True)
    gale_status = models.CharField(max_length=10, null=True, blank=True)
    small_craft_status = models.CharField(max_length=10,null=True, blank=True)
    met_sit_head = models.TextField(null=True, blank=True)
    met_sit_time = models.CharField(max_length=250)
    met_sit_text = models.TextField(null=True, blank=True)
    outlook_time = models.CharField(max_length=250, null=True, blank=True)
    outlook_head = models.TextField(null=True, blank=True)
    outlook_text = models.TextField(null=True, blank=True)
    swell_status = models.CharField(max_length=210, null=True, blank=True)
    swell_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.issued_time

    class Meta:
        verbose_name_plural = 'sea area forecasts met ie'


class MetOceanBuoyData(models.Model):
    EightHourlyID = models.IntegerField()
    MMSI = models.IntegerField()
    AverageWindSpeed = models.IntegerField(null=True, blank=True)
    GustSpeed = models.IntegerField(null=True, blank=True)
    WindDirection = models.IntegerField(null=True, blank=True)
    WindGustDirection = models.IntegerField(null=True, blank=True)
    AirTemperature = models.FloatField(null=True, blank=True)
    RelativeHumidity = models.IntegerField(null=True, blank=True)
    DewPoint = models.FloatField(null=True, blank=True)
    AirPressure = models.IntegerField(null=True, blank=True)
    PressureTendency = models.IntegerField(null=True, blank=True)
    HorizVisibility = models.FloatField(null=True, blank=True)
    WaterLevel = models.FloatField(null=True, blank=True)
    WaterLevelTrend = models.IntegerField(null=True, blank=True)
    SurfaceCurrentSpeed = models.IntegerField(null=True, blank=True)
    SurfaceCurrentDirection = models.IntegerField(null=True, blank=True)
    CurrentSpeed2 = models.IntegerField(null=True, blank=True)
    CurrentDirection2 = models.IntegerField(null=True, blank=True)
    MeasurementDepth2 = models.IntegerField(null=True, blank=True)
    CurrentSpeed3 = models.IntegerField(null=True, blank=True)
    CurrentDirection3 = models.IntegerField(null=True, blank=True)
    MeasurementDepth3 = models.IntegerField(null=True, blank=True)
    WaveHeight = models.FloatField(null=True, blank=True)
    WavePeriod = models.IntegerField(null=True, blank=True)
    WaveDirection = models.IntegerField(null=True, blank=True)
    SwellHeight = models.FloatField(null=True, blank=True)
    SwellPeriod = models.IntegerField(null=True, blank=True)
    SwellDirection = models.IntegerField(null=True, blank=True)
    SeaState = models.IntegerField(null=True, blank=True)
    WaterTemperature = models.FloatField(null=True, blank=True)
    Precipitation = models.IntegerField(null=True, blank=True)
    Salinity = models.FloatField(null=True, blank=True)
    Ice = models.CharField(null=True, blank=True)
    DateTransmitted = models.DateTimeField()

    def __str__(self):
        return self.DateTransmitted.strftime("%Y-%m-%d %H:%M:%S") if self.DateTransmitted else "No Date"

    class Meta:
        verbose_name_plural = 'met ocean buoy data'

class MetIeBuoyData(models.Model):

    station_id = models.CharField(max_length=20)
    CallSign = models.CharField(max_length=20)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    AtmosphericPressure = models.FloatField(null=True, blank=True)
    WindDirection = models.FloatField(null=True, blank=True)
    WindSpeed = models.FloatField(null=True, blank=True)
    Gust = models.FloatField(null=True, blank=True)
    WaveHeight = models.FloatField(null=True, blank=True)
    WavePeriod = models.FloatField(null=True, blank=True)
    MeanWaveDirection = models.FloatField(null=True, blank=True)
    Hmax = models.FloatField(null=True, blank=True)
    AirTemperature = models.FloatField(null=True, blank=True)
    DewPoint = models.FloatField(null=True, blank=True)
    SeaTemperature = models.FloatField(null=True, blank=True)
    salinity = models.FloatField(null=True, blank=True)
    RelativeHumidity = models.FloatField(null=True, blank=True)
    SprTp = models.FloatField(null=True, blank=True)
    ThTp = models.FloatField(null=True, blank=True)
    Tp = models.FloatField(null=True, blank=True)
    QC_Flag = models.FloatField(null=True, blank=True)

    def __str__(self):
        # Format the time field as a string
        time_str = self.time.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.station_id} - {time_str}"

    class Meta:
        verbose_name_plural = 'irish lights buoy data'

class WeatherBuoy(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    mmsi = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'weather buoys'

class SourceFormat(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'source formats'


class SourceURL(models.Model):
    name = models.CharField(max_length=25)
    url = models.CharField(max_length=500)
    description = models.CharField(max_length=250, blank=True, null=True)
    format = models.ForeignKey(SourceFormat, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'source urls'
