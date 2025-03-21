from django.urls import path
from .views import (SourceFormatListView, SourceFormatDetailView, 
                    SourceFormatCreateView, SourceFormatUpdateView,
                    SourceFormatDeleteView, Home, SourceURLListView,
                    SourceURLDetailView, SourceURLCreateView, SourceURLUpdateView,
                    SourceURLDeleteView, latest_forecast_view, 
                    TeamView, DwdView, CoastWarningsDWDView)

urlpatterns = [
    #path('', Home.as_view(), name='home'),
    path('', latest_forecast_view, name='home'),
    path('sourceformat/', SourceFormatListView.as_view(), name='sourceformat_list'),
    path('sourceformat/<int:pk>/', SourceFormatDetailView.as_view(), name='sourceformat_detail'),
    path('sourceformat/add/', SourceFormatCreateView.as_view(), name='sourceformat_add'),
    path('sourceformat/<int:pk>/edit/', SourceFormatUpdateView.as_view(), name='sourceformat_edit'),
    path('sourceformat/<int:pk>/delete/', SourceFormatDeleteView.as_view(), name='sourceformat_delete'),
    # Add similar paths for SourceURL
    path('sourceurl/', SourceURLListView.as_view(), name='sourceurl_list'),
    path('sourceurl/<int:pk>/', SourceURLDetailView.as_view(), name='sourceurl_detail'),
    path('sourceurl/add/', SourceURLCreateView.as_view(), name='sourceurl_add'),
    path('sourceurl/<int:pk>/edit/', SourceURLUpdateView.as_view(), name='sourceurl_edit'),
    path('sourceurl/<int:pk>/delete/', SourceURLDeleteView.as_view(), name='sourceurl_delete'),
    # Weather Forecasts
    path('latest-forecast/', latest_forecast_view, name='latest_forecast'),
    # Team site
    path('team/', TeamView.as_view(), name='team'),
    # DWD site (German weather service)
    path('dwd/', DwdView.as_view(), name='dwd'),
    path('dwdcoastwarnings/', CoastWarningsDWDView.as_view(), name='dwdcoastwarnings' )
]
