from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView

from apps.review.forms import ReviewForm
from apps.review.models import Review
from apps.airport.models import Rates, Airport


class Create(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/create.html'
    success_url = '/mypage/'

    def form_valid(self, form):
        review = form.save(commit=False)
        review.author = self.request.user
        review.save()

        update_airport_rate(self, review)

        return redirect('/mypage/')


class Update(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/edit.html'
    success_url = '/mypage/'

    def form_valid(self, form):
        review = form.save()
        update_airport_rate(self, review)

        return super(Update, self).form_valid(form)


@login_required
def delete(request, pk):
    review = get_object_or_404(Review, id=pk)
    if (request.user.id != review.author_id):
        return redirect('/mypage/')

    review.delete()
    return redirect('/mypage/')


def update_airport_rate(self, review):
    # insert record into rates table
    item = Airport.objects.get(pk=review.airport_id)
    query = Rates.objects.filter(user=self.request.user, item=item)
    if query.count() == 0:
        Rates.objects \
            .create(
                user=self.request.user,
                item=item,
                created_at=datetime.now(),
                rate=review.rate
            )
    else:
        query \
            .update(
                created_at=datetime.now(),
                rate=review.rate
            )

    # update airport rate
    avg = Rates.objects.filter(item=item).aggregate(Avg('rate'))
    item.rate = avg['rate__avg']
    item.save()
