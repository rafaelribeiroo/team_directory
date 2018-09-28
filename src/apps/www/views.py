from django.shortcuts import render
from .models import Person


def index(request):
    person = Person.objects.all()
    context = {
        'peoples': person,
    }
    return render(request, 'index.html', context)


def detail(request, slug):
    pass
