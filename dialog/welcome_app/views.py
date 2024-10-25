from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(60)
def welcome_page(request):
    template = 'welcome/welcome.html'
    context = {}
    return render(request, template, context)
