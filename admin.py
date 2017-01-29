from django.contrib import admin
from django.contrib.sites.models import Site

from image_cropping import ImageCroppingMixin

from .models import Church, News
from .forms import ChurchForm

admin.site.site_header = "Churches of Bridlington Administration"

class ChurchAdmin(ImageCroppingMixin, admin.ModelAdmin):
    form = ChurchForm
    fieldsets = (
        (
            "Basic Info", {
                'fields': ('name', 'classification', 'short_description', 'long_description')
            },
        ),
        (
            "Photo", {
                'fields': ('photo', 'wide_crop', 'list_crop')
            },
        ),
        (
            "Address", {
                'fields': ('address_line_1', 'address_line_2', 'postcode', 'map_embed_link', 'show_map')
            },
        ),
        (
            "Contact", {
                'fields': ('email', 'phone_number', 'website')
            },
        )
    )

class NewsAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = News
    fieldsets = (
        (
            "Text", {
                'fields': ('title', 'blurb', 'text')
            },
        ),
        (
            "Photo", {
                'fields': ('photo', 'square_crop', 'photo_caption', 'photo_description')
            },
        ),
        (
            "Admin", {
                'fields': ('publish',)
            },
        ),
    )

admin.site.register(Church, ChurchAdmin)
admin.site.register(News, NewsAdmin)
