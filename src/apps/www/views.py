from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Person
from .forms import PersonForm
from django.forms.models import model_to_dict


def index(request):
    if request.user.is_authenticated:
        person = Person.objects.all()
        context = {
            'peoples': person,
        }
        return render(request, 'index.html', context)
    else:
        redirect('/login/google-oauth2')


def detail(request, year, month, day, slug):
    person = Person.objects.get(slug=slug, birthday__year=year, birthday__month=month, birthday__day=day)
    return render(request, 'detail.html', {'person': person})


def edit(request, slug):
    person = Person.objects.get(slug=slug)
    if request.method == 'POST':
        # Process the form
        form = PersonForm(data=request.POST, instance=person)
        if form.is_valid():
            form.save(commit=True)
        return redirect(reverse('www:detail', args=[slug, ]))
    else:
        person_dict = model_to_dict(person)
        form = PersonForm(person_dict)
        return render(request, 'edit.html', {'form': form})


def verify_email(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        existing_person = Person.objects.filter(email=kwargs.get('www:detail').get('email'))
        if not existing_person:
            return HttpResponse('You dont have access!')
