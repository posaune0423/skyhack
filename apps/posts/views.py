from django.shortcuts import render

from apps.orater.post import Post


def top(request):
    return render(request, 'index.html')


def index(request):
    posts = Post \
        .order_by('pub_date', 'desc') \
        .limit(5) \
        .get()

    return render(request, 'posts/index.html', {'posts': posts})


def show(request, id):
    post = Post \
        .where('id', id) \
        .first()

    return render(request, 'posts/show.html', {'post': post})
