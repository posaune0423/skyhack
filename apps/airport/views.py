from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.orater.airport import Airport
from apps.orater.review import Review


@login_required
def index(request):
    country = request.GET.get('country')
    if country:
        airports = Airport \
            .where('country', country) \
            .take(6) \
            .get()
    else:
        airports = Airport \
            .order_by('created_at', 'desc') \
            .take(6) \
            .get()

    return render(request, 'airport/index.html', {'airports': airports})


@login_required
def search(request):
    target = request.GET.get('q')
    if target:
        airports = Airport \
            .where('title', 'like', f'%{target}%') \
            .order_by('created_at', 'desc') \
            .get()
    else:
        airports = None

    return render(request, 'search.html', {'airports': airports})


@login_required
def show(request, pk):
    airport = Airport.objects.get(id=pk)
    reviews = Review.objects \
        .filter(airport=airport.id) \
        .all()

    return render(request, 'airport/show.html', {'airport': airport, 'reviews': reviews})


def top(request):
    return render(request, 'index.html')


def notfound(request):
    return render(request, '404.html')
