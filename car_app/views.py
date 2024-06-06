from django.shortcuts import render
from django.views.generic import ListView

from .models import Auto


# def cars_list(request):
#     cars = Auto.objects.all()
#     context = {
#         'title': 'Автомобили',
#         'cars': cars
#     }
#     return render(request, 'car_list.html', context)


class AutoListView(ListView):
    model = Auto
    template_name = 'car_list.html'
    context_object_name = 'cars'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Автомобили'
        return context
