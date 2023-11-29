from django.shortcuts import render, get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import SeaAreaForecastMet, WeatherForecastCoast


def latest_forecast_view(request):
    # Get the most recent SeaAreaForecastMet instance
    latest_forecast = SeaAreaForecastMet.objects.order_by('-issued_time').first()

    # Get all associated WeatherForecastCoast instances
    if latest_forecast:
        weather_coasts = WeatherForecastCoast.objects.filter(sea_area_forecast_met=latest_forecast)
    else:
        weather_coasts = WeatherForecastCoast.objects.none()

    # Prepare the context for the template
    context = {
        'latest_forecast': latest_forecast,
        'weather_coasts': weather_coasts,
    }

    return render(request, 'sea_area_forecast_latest.html', context)
