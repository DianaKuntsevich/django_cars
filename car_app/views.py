from django.shortcuts import render

from .models import Auto


def cars_list(request):
    cars = Auto.objects.all()
    context = {
        'title': 'Автомобили',
        'cars': cars
    }
    return render(request, 'car_list.html', context)

