from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import json
from django.conf import settings
import os
from .forms import ArtistForm
def search(request):
    return render(request, 'search_app/search.html')

def autocomplete(request):
    if 'term' in request.GET:
        term = request.GET.get('term').lower()
        file_path = os.path.join(settings.BASE_DIR, 'static', 'data.json')

        if os.path.exists(file_path):
            print(f"Loading data from: {file_path}")
            with open(file_path, 'r') as f:
                data = json.load(f)
                print(f"Data loaded: {data}")

            results = [item['name'] for item in data if term in item['name'].lower()]
            print(f"Filtered results: {results}")
            return JsonResponse(results, safe=False)
        else:
            print("data.json not found in static files")
            return JsonResponse([], safe=False)

    return JsonResponse([], safe=False)

def select_artist(request):
    if request.method == 'GET':
        form = ArtistForm(request.GET)
        if form.is_valid():
            artist_name = form.cleaned_data['name']
            Artist.objects.create(name=artist_name)
            return redirect('recent_artist')
    else:
        form = ArtistForm()
    return render(request, 'search_app/search.html', {'form': form})

def recent_artist(request):
    recent_artist = Artist.objects.order_by('-selected_at').first()
    if recent_artist:
        return HttpResponse(f"The most recent artist selected is: {recent_artist.name}")
    else:
        return HttpResponse("No artist has been selected yet.")
    
    