from django.contrib import admin

# import your models here
from .models import Medication

# Register your models here
admin.site.register(Medication)