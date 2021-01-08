from django.contrib import admin
from .models import *


# Register your models here.

class BOQAdmin(admin.ModelAdmin):
    list_display = ["boqcodes","category", "material","objecttype"]
    list_filter = ["category", "material"]
    search_fields = ["category"]

    class Meta:
        model = setboq


admin.site.register(setboq, BOQAdmin)
