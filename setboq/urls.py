from django.urls import path
from .views import *

app_name = "setboq"

urlpatterns = [
    path('setboq/index/', index_boq, name="index"),
    path('setboq/<int:id>/detail', detail_boq, name="detail"),
    path('setboq/', set_boq, name="set"),
    path('<int:id>/delete', delete_boq, name="delete"),
    path('<int:id>/update', update_boq, name="update"),
    path('getboq/', get_boq, name="get")

]