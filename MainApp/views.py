from django.shortcuts import render, get_object_or_404
import json
from django.http import Http404
from MainApp.models import Country, Language


def home_page(request):
    return render(request, 'home.html')

def countries_list(request):
    countries = Country.objects.all()
    context = {
        'countries': countries,
    }
    return render(request, 'countries_list.html', context)


def country_detail(request, country_name):
    country = get_object_or_404(Country, country=country_name)
    context = {
        'country': country,
    }
    return render(request, 'country_detail.html', context)


def languages_view(request):
    languages = Language.objects.all().order_by('language')

    context = {
        'languages': languages,
    }
    return render(request, 'languages.html', context)