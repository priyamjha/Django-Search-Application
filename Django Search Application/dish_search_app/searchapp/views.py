from django.shortcuts import render
from django.db.models import Q
from .models import Restaurant

def search_dish(request):
    query = request.GET.get('q')
    if query:
        results = Restaurant.objects.filter(items__icontains=query)
    else:
        results = Restaurant.objects.none()
    return render(request, 'searchapp/index.html', {'query': query, 'results': results})
