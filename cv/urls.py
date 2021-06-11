from .views import AccueilView, Portfolio1View
from django.urls import path

app_name = "cv"

urlpatterns = [
    path('accueil/', AccueilView.as_view(), name="accueil"),
    path('portfolio1', Portfolio1View.as_view(), name="portfolio1")
]
