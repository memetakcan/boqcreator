from django.contrib import admin
from .models import *


# Register your models here.

class BOQAdmin(admin.ModelAdmin):
    list_display = ["category", "material"]
    list_filter = ["category", "material"]
    search_fields = ["category"]

    class Meta:
        model = getboq


admin.site.register(getboq, BOQAdmin)
