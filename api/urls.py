from django.urls import path
from .views import *

urlpatterns = [
    path ('function/',function_api, name='function_api')
]