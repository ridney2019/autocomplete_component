from django.http import JsonResponse
from search_app.models import Item
from django.shortcuts import render

def search(request):
    return render(request, 'search_app/search.html')

def autocomplete(request):
    if 'term' in request.GET:
        qs = Item.objects.filter(name__icontains=request.GET.get('term'))
        names = list(qs.values_list('name', flat=True))
        return JsonResponse(names, safe=False)
    return JsonResponse([], safe=False)

