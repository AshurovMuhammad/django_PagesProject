from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class PersonPageView(TemplateView):
    template_name = 'person.html'

class DreamPageView(TemplateView):
    template_name = 'dream.html'