from django.shortcuts import render, redirect
from .models import OurMenuModel, CoffeesModel, CroissantsModel


def index(request):
    our_menus = OurMenuModel.objects.all()
    return render(request, 'layouts/home.html', context={'our_menus': our_menus})


def coffees(request):

    tmp = CoffeesModel.objects.all()
    return render(request, template_name='coffees.html', context={
        'coffee': tmp
    })

def croissants(request):
    cr = CroissantsModel.objects.all()
    return render(request, template_name='croissants.html', context={
        'croissant': cr
    })

def our_menu(request):
    tmp = CoffeesModel.objects.all()
    cr = CroissantsModel.objects.all()
    return render(request, template_name='our_menu.html', context={
        'coffee': tmp,
        'croissant': cr
    })

