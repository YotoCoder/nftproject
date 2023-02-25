from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 1.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("El tamaño maximo de subida es de %sMB" % str(megabyte_limit))

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True, validators=[validate_image])
    roll = models.CharField(max_length=12, null=True, blank=True)

    ip = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)