from django.shortcuts import render
from .models import Person


def index(request):
    person = Person.objects.all()
    context = {
        'peoples': person,
    }
    return render(request, 'index.html', context)


def detail(request, slug, email):
    person = Person.objects.get(slug=slug, email=email)
    return render(request, 'detail.html', {'person': person})
