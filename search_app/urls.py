from django.urls import path
from .views import search, autocomplete

urlpatterns = [
    path('', search, name='search'),
    path('autocomplete/', autocomplete, name='autocomplete'),
]
