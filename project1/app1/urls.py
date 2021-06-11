from django.urls import path
from .views import *
app_name = 'Home'

urlpatterns = [
    path('home/', home ,name='Home'),
    path('common/',common),
    
]
