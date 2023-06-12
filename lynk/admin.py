"""Connecting the lynk app to Django Admin"""

from django.contrib import admin
from .models import User, Element

# Register your models here.
admin.site.register(Element)
admin.site.register(User)
