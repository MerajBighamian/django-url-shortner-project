from django.db import models

# Create your models here.

# for save url (recive from users)
class Urls(models.Model):

    # define verbose name plural
    class Meta:
        # verbose name plural is Urls
        verbose_name_plural = 'Urls'

    # field for save links ( some urls is very long )
    links = models.CharField(max_length=10000)

    # field for save uuid of a link record (for pass users to orginal urls)
    uuid = models.CharField(max_length=10)