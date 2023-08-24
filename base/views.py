from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    UpdateView, DeleteView, CreateView)

from .models import *


class HomeView(ListView):
    model = Dish
    allow_empty = True
    template_name = "base/home.html"
    context_object_name = "dishes"
    ordering = '-pk',
    extra_context = {'title': 'Home'}


class DishCreateView(CreateView):
    model = Dish
    fields = "__all__"
    template_name = "base/form.html"
    extra_context = {'title': 'Create', 'submit': 'create',
                     'is_file': True}


class DishView(DetailView):
    model = Dish
    template_name = 'base/dish.html'
    context_object_name = "dish"


class DishUpdateView(UpdateView):
    model = Dish
    fields = "__all__"
    template_name = "base/form.html"
    extra_context = {'title': 'Update', 'submit': 'update',
                     'is_file': True}

class DishDeleteView(DeleteView):
    model = Dish
    template_name = "base/confirm.html"
    success_url = reverse_lazy('home')
