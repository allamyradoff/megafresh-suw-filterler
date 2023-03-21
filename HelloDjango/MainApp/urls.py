from django.urls import path
from MainApp.views import *


urlpatterns = [
    path('', index, name='index'),
]
