from django.contrib import admin
from django.contrib.sites.models import Site

from .models import Church

admin.site.site_header = "Churches of Bridlington Administration"

admin.site.register(Church)
admin.site.unregister(Site)
