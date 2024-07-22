from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import json
from django.conf import settings
import os

def search(request):
    return render(request, 'search_app/search.html')

recent_searches = []

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

            # Store recent search in session
            if 'recent_searches' not in request.session:
                request.session['recent_searches'] = []
            recent_searches = request.session['recent_searches']
            for result in results:
                if result not in recent_searches:
                    recent_searches.append(result)
                    if len(recent_searches) > 10:  # Limit to 10 recent searches
                        recent_searches.pop(0)
            request.session['recent_searches'] = recent_searches

            return JsonResponse(results, safe=False)
        else:
            print("data.json not found in static files")
            return JsonResponse([], safe=False)

    return JsonResponse([], safe=False)