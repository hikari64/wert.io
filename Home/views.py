from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    template = get_template('homepage.html')
    html = template.render()
    return HttpResponse(html)
