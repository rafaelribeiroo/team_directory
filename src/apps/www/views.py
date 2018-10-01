from django.shortcuts import render
from .models import Person
from .forms import PersonForm


def index(request):
    person = Person.objects.all()
    context = {
        'peoples': person,
    }
    return render(request, 'index.html', context)


def detail(request, year, month, day, slug):
    person = Person.objects.get(slug=slug, birthday__year=year, birthday__month=month, birthday__day=day)
    return render(request, 'detail.html', {'person': person})


def edit(request, slug):
    form = PersonForm()
    return render(request, 'edit.html', {'form': form})
