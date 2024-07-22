from django.urls import path
from .views import search, autocomplete, select_artist, recent_artist

urlpatterns = [
    path('', search, name='search'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    # path('select-artist/', select_artist, name='select_artist'),
    # path('recent-artist/', recent_artist, name='recent_artist'),
]
