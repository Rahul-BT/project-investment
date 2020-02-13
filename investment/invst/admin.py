from django.contrib import admin

from .models import Invst, Dental, MF
# Register your models here.

admin.site.register(Invst)
admin.site.register([Dental, MF])