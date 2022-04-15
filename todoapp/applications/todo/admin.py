from django.contrib import admin
from django.contrib.admin import register
from . import models


@register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    pass
