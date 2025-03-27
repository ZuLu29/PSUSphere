from django.shortcuts import render
from django.views.generic.list import ListView
from studentorg.models import Organization


class HomePageView(ListView):
    model = Organization
    context_object_name = "home"  # Changed from 'home' to be more descriptive
    template_name = "home.html"


# Create your views here.
