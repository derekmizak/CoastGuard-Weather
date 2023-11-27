from django.contrib import admin

# Register your models here.
from .models import SourceFormat, SourceURL


admin.site.register(SourceFormat)

admin.site.register(SourceURL)

