import hashlib

from django.db import models
from django.urls import reverse


class TimedatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='created at', db_index=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False, verbose_name='modified at', db_index=True)

    class Meta:
        abstract = True


class IsActiveModel(models.Model):
    is_active = models.BooleanField(verbose_name='active', default=True)

    class Meta:
        abstract = True


class AdminChangeUrlModel(models.Model):
    @property
    def admin_change_url(self):
        return reverse(
            'admin:{}_{}_change'.format(self._meta.app_label, self._meta.model_name), args=[self.id]
        )

    class Meta:
        abstract = True


def _image_upload(instance, filename):
    image_path = '{instance_name}/file/{filename}.{extension}'.format(
        instance_name=type(instance).__name__.lower(),
        filename=hashlib.sha1(instance.image.read()).hexdigest(),
        extension=filename.rpartition('.')[-1]
    )
    return image_path


class ImageModel(models.Model):
    image = models.ImageField(
        max_length=512, verbose_name='image', upload_to=_image_upload
    )

    class Meta:
        abstract = True
