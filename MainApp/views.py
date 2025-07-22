from django.shortcuts import render
import json
from django.http import Http404

def load_countries():
    with open('countries.json', encoding="utf-8") as json_file:
        return json.load(json_file)
def home_page(request):
    return render(request, 'home.html')

def countries_list(request):
    countries = load_countries()
    context = {
        'countries': countries,
    }
    return render(request, 'countries_list.html', context)


def country_detail(request, country_name):
    countries = load_countries()
    for country in countries:
        if country['country'] == country_name:
            context = {
                'country': country,
            }
            return render(request, 'country_detail.html', context)

    raise Http404("Страна не найдена")

