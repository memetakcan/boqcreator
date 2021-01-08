from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index_boq, name="index"),
    path('get/<int:id>/detail', detail_boq, name="detail"),
    path('get/', get_boq, name="get"),
]