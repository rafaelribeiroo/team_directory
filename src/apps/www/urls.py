from django.urls import path
from .views import (
    index,
)


app_name = 'www'
urlpatterns = [
    path('', index, name='home'),
]
