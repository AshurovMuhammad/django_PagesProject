from django.urls import path
from .views import HomePageView, AboutPageView, PersonPageView, DreamPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('person/', PersonPageView.as_view(), name='person'),
    path('dream/', DreamPageView.as_view(), name='dream')
]