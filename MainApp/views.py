from django.shortcuts import render, get_object_or_404
import json
from django.http import Http404
from MainApp.models import Country, Language


def home_page(request):
    return render(request, 'home.html')

def countries_list(request):
    alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    countries = Country.objects.all()
    context = {
        'countries': countries,
        'alphabet': alphabet,
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


def language_detail(request, lang):
    language = get_object_or_404(Language, language=lang)
    countries = language.countries.all()
    context = {
        'language': language,
        'countries': countries,
    }
    return render(request, 'language_detail.html', context)


def countries_by_letter(request, letter):
    alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    countries = Country.objects.filter(country__istartswith=letter)
    context = {
        'alphabet': alphabet,
        'countries': countries,
        'letter': letter,

    }
    return render(request, 'countries_by_letter.html', context)