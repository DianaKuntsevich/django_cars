from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Auto


class AutoListView(ListView):
    model = Auto
    template_name = 'aw_cars/car_list.html'
    context_object_name = 'cars'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Автомобили'
        return context




class AutoDetailView(DetailView):
    model = Auto
    template_name = 'aw_cars/car_detail.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.model
        return context
