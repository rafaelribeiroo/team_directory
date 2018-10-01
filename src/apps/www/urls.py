from django.urls import path
from .views import (
    index,
    detail,
)


app_name = 'www'
urlpatterns = [
    path('', index, name='home'),
    path('members/<str:slug>/<str:email>/', detail, name='detail'),
]
