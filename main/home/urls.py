from django.urls import path
from .views import *


urlpatterns = [
    path('', base, name='base'),
    path('drevo/', drevo, name='drevo'),
    path('search/', search, name='search'),

]
