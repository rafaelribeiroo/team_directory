from django.shortcuts import render, redirect, reverse
from .models import Person
from .forms import PersonForm
from django.forms.models import model_to_dict


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
    person = Person.objects.get(slug=slug)
    if request.method == 'POST':
        # Process the form
        form = PersonForm(data=request.POST, instance=person)
        if form.is_valid():
            form.save(commit=True)
        return redirect(reverse('detail', args=[slug, ]))
    else:
        person_dict = model_to_dict(person)
        form = PersonForm(person_dict)
        return render(request, 'edit.html', {'form': form})
