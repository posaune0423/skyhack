from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.review.forms import ReviewForm
from apps.orater.review import Review


@login_required
def create(request):
    form = ReviewForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/mypage/')

    return render(request, 'review/create.html', {'form': form})


@login_required
def update(request, id):
    form = ReviewForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/mypage/')

    review = Review.find(id)
    fields = {
        "title": review.title,
        'body': review.body,
        "created_at": review.created_at,
        "author": review.author_id,
        "airport": review.airport_id,
        "rate": review.rate,
    }

    form = ReviewForm(fields)
    return render(request, 'review/edit.html', {'form': form})


@login_required
def delete(request, id):
    review = Review.find(id)
    if (request.user.id != review.author_id):
        return redirect('/mypage/')

    review.delete()
    return redirect('/mypage/')
