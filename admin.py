from django.contrib import admin
from django.contrib.sites.models import Site

from image_cropping import ImageCroppingMixin

from .models import Church
from .forms import ChurchForm

admin.site.site_header = "Churches of Bridlington Administration"

class ChurchAdmin(ImageCroppingMixin, admin.ModelAdmin):
    form = ChurchForm

admin.site.register(Church, ChurchAdmin)
