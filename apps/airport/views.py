from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView

from apps.airport.models import Airport
from apps.review.models import Review


class Index(ListView):
    template_name = 'airport/index.html'
    context_object_name = 'airports'

    def get_queryset(self):
        country = self.request.GET.get('country')
        country = country.strip()

        if country:
            object_list = Airport.objects \
                              .filter(country=country) \
                              .order_by('-created_at')[:6]
        else:
            object_list = Airport.objects \
                              .filter(created_at__lte=timezone.now()) \
                              .order_by('-created_at')[:6]
        return object_list


class Search(ListView):
    template_name = 'search.html'
    context_object_name = 'airports'

    def get_queryset(self):
        q_word = self.request.GET.get('q')
        q_word = q_word.strip()

        if q_word:
            object_list = Airport.objects \
                              .filter(Q(title__icontains=q_word) | Q(body__icontains=q_word)) \
                              .order_by('-created_at')[:6]
        else:
            object_list = None
        return object_list


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
