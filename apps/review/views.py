from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView

from apps.review.forms import ReviewForm
from apps.review.models import Review


class Create(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/create.html'
    success_url = '/mypage/'

    def form_valid(self, form):
        review = form.save(commit=False)
        review.author = self.request.user
        review.save()

        return redirect('/mypage/')


class Update(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/edit.html'
    success_url = '/mypage/'


@login_required
def delete(request, pk):
    review = get_object_or_404(Review, id=pk)
    if (request.user.id != review.author_id):
        return redirect('/mypage/')

    review.delete()
    return redirect('/mypage/')
