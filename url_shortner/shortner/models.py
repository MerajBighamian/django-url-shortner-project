
from django.db import models
# from django.contrib.auth.models import User
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

    ## TODO : define user field for specify user of url shortnerd
    # user field
    # user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    