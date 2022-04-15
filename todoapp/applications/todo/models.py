from django.conf import settings
from django.db import models
from todoapp import abstract_models as am


class Task(
    am.TimedatedModel,
    am.ImageModel,
    am.AdminChangeUrlModel,
):
    user = models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='name', max_length=255)
    description = models.TextField(verbose_name='description')
    deadline = models.DateField(verbose_name='deadline', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
