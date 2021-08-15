from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(StateWiseTestingDetails)
admin.site.register(StateWiseTesting)
admin.site.register(StateWiseCovidDetails)
