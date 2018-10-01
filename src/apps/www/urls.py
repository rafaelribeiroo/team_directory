from django.urls import path, re_path
from .views import (
    index,
    detail,
    edit,
)


app_name = 'www'
urlpatterns = [
    path('', index, name='home'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<slug>[\w-]+)$', detail, name='detail'),
    # path('members/<str:slug>/<str:birthday>/', detail, name='detail'),
    path('members/<str:slug>/', edit, name='edit'),
]
