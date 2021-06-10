from django.views.generic.base import TemplateView
import datetime


# Create your views here.
class AccueilView(TemplateView):
    """ That class to get the acceuil page"""
    template_name = "cv/accueil.html"


class Portfolio1View(TemplateView):
    """ That class to get the acceuil page"""
    template_name = "cv/portfolio-1.html"