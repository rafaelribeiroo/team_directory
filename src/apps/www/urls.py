from django.urls import path, re_path
from .views import (
    index,
    detail,
)


app_name = 'www'
urlpatterns = [
    path('', index, name='home'),
    re_path(r'^members/([a-z0-9-]+)/', detail, name='detail'),
]
