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
    wide_crop = ImageRatioField('photo', '768x200', size_warning=True)
    list_crop = ImageRatioField('photo', '250x200', size_warning=True)
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
    map_query = models.CharField(max_length=200, blank=True, editable=False, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        self.map_query = ", ".join([self.address_line_1, self.address_line_2, self.postcode, "United Kingdom"])
        super(Church, self).save(*args, **kwargs)

    def __str__(self):
        return "{}, {}".format(self.name, self.address_line_2)


class News(models.Model):

    class Meta:
        verbose_name_plural = "News"
        ordering = ("-datetime",)

    title = models.CharField(max_length=64)
    blurb = models.CharField(max_length=144, help_text="Tweet length (144 characters). Optional.", blank=True)
    text = models.TextField()
    photo = models.ImageField(blank=True)
    photo_description = models.CharField(max_length=256, blank=True, help_text="Optional description (useful for screen readers).")
    photo_caption = models.TextField(blank=True)
    square_crop = ImageRatioField('photo', '64x64', size_warning=True)
    publish = models.BooleanField(default=False, help_text="Select when the article is ready for publication.")
    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}: {}".format(str(self.date), str(self.title))
