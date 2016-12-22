from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify

from image_cropping import ImageRatioField


class Church(models.Model):
    class Meta:
        verbose_name_plural = "Churches"
    name = models.CharField(max_length=64)
    short_description = models.CharField(max_length=128)
    long_description = models.TextField()
    photo = models.ImageField(blank=True)
    wide_crop = ImageRatioField('photo', '768x180')
    list_crop = ImageRatioField('photo', '280x180')
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

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Church, self).save(*args, **kwargs)

    def __str__(self):
        return "{}, {}".format(self.name, self.address_line_2)
