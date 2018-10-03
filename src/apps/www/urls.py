from django.urls import path
from .views import (
    index,
    detail,
    edit,
)


app_name = 'www'
urlpatterns = [
    path('', index, name='home'),
    path('members/<int:year>/<int:month>/<int:day>/<str:slug>', detail, name='detail'),
    path('members/<str:slug>/edit/', edit, name='edit'),
]
