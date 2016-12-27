import urllib

from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify

from image_cropping import ImageRatioField


class Church(models.Model):
    class Meta:
        verbose_name_plural = "Churches"
        ordering = ['name']
    name = models.CharField(max_length=64)
    CLASSIFICATION_CHOICES = (
        ('T', 'Town'),
        ('V', 'Village'),
    )
    classification = models.CharField(
        max_length=1,
        choices=CLASSIFICATION_CHOICES,
        default='T'
    )
    short_description = models.CharField(max_length=128)
    long_description = models.TextField()
    photo = models.ImageField(blank=True)
    wide_crop = ImageRatioField('photo', '768x180')
    list_crop = ImageRatioField('photo', '400x300')
    address_line_1 = models.CharField(max_length=64)
    address_line_2 = models.CharField(max_length=64)
    postcode_regex = RegexValidator(
        regex=r'^([a-zA-Z](([0-9][0-9]?)|([a-zA-Z][0-9][0-9]?)|([a-zA-Z]?[0-9][a-zA-Z]))'
              r' ?[0-9][abd-hjlnp-uw-zABD-HJLNP-UW-Z]{2})$', message="Invalid postcode.")
    postcode = models.CharField(max_length=10, validators=[postcode_regex])
    email = models.EmailField(blank=True)
    phone_regex = RegexValidator(
        regex=r'^[ \d]{6,20}$',
        message="Phone number bust be a sequence of numbers or spaces."
    )
    phone_number = models.CharField(blank=True, max_length=20)
    website = models.URLField(blank=True)
    slug = models.SlugField(editable=False, unique=True)

    show_map = models.BooleanField(default=True, help_text="Choose whether or not to display the location of the church as a Google map.")
    map_query = models.CharField(max_length=200, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        self.map_query = ", ".join([self.address_line_1, self.address_line_2, self.postcode, "United Kingdom"])
        super(Church, self).save(*args, **kwargs)

    def __str__(self):
        return "{}, {}".format(self.name, self.address_line_2)
