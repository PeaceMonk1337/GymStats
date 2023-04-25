from django.shortcuts import render
from django.db.models import Q
from obludarium.models import Atlet,Vykon
from .forms import SearchForm

def search(request):
    query = request.GET.get("q")
    if query:
        queryset = (
            Q(atlet__icontains=query) |
            Q(vykon__icontain=query)
        )
        results = Atlet.objects.filter(queryset) | Vykon.objects.filter(queryset)
    else:
        results = []
    return render(request,"search/search_results.html", {'results':results})


# Create your views here.
