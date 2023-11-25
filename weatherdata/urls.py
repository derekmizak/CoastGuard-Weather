from django.urls import path
from .views import (SourceFormatListView, SourceFormatDetailView, 
                    SourceFormatCreateView, SourceFormatUpdateView, SourceFormatDeleteView, Home, SourceURLListView, SourceURLDetailView, SourceURLCreateView, SourceURLUpdateView, SourceURLDeleteView)

urlpatterns = [
    path('', Home.as_view(), name='home'),
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
]
