from django.urls import path
from RuApp.views import *


urlpatterns = [
    path('', index, name='Ruindex'),
]
