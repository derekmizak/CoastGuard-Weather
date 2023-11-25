from django.urls import path
from .views import (SourceFormatListView, SourceFormatDetailView, 
                    SourceFormatCreateView, SourceFormatUpdateView, SourceFormatDeleteView, Home)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('sourceformat/', SourceFormatListView.as_view(), name='sourceformat_list'),
    path('sourceformat/<int:pk>/', SourceFormatDetailView.as_view(), name='sourceformat_detail'),
    path('sourceformat/add/', SourceFormatCreateView.as_view(), name='sourceformat_add'),
    path('sourceformat/<int:pk>/edit/', SourceFormatUpdateView.as_view(), name='sourceformat_edit'),
    path('sourceformat/<int:pk>/delete/', SourceFormatDeleteView.as_view(), name='sourceformat_delete'),
    # Add similar paths for SourceURL
]
