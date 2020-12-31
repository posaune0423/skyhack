from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView

from apps.review.forms import ReviewForm
from apps.review.models import Review


class Create(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/create.html'
    success_url = '/mypage/'


class Update(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/edit.html'


def delete(request, pk):
    post = get_object_or_404(Review, id=pk)
    if (request.user.id != post.author_id):
        return redirect('/mypage/')

    post.delete()
    return redirect('/mypage/')
