from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.orater.post import Post


def top(request):
    return render(request, 'index.html')


@login_required
def index(request):
    posts = Post \
        .order_by('pub_date', 'desc') \
        .limit(5) \
        .get()

    return render(request, 'posts/index.html', {'posts': posts})


@login_required
def show(request, id):
    post = Post \
        .where('id', id) \
        .first()

    return render(request, 'posts/show.html', {'post': post})

@login_required
def create(request, params):
    post = {
        'title': params['title'],
        'body': params['body'],
        'pub_date': params['pub_date'],
        'country': params['country'],
        'image_path': params['image_path'],
        'image_path2': params['image_path2'],
        'image_path3': params['image_path3'],
        'image_path4': params['image_path4'],
        'image_path5': params['image_path5'],
        'author_id': params['author_id'],
        'rate': params['rate'],
    }

    return Post\
        .insert(post)


@login_required
def update(request, id, params):
    params = {
        'title': params['title'],
        'body': params['body'],
        'country': params['country'],
        'image_path': params['image_path'],
        'image_path2': params['image_path2'],
        'image_path3': params['image_path3'],
        'image_path4': params['image_path4'],
        'image_path5': params['image_path5'],
        'rate': params['rate'],
    }

    return Post\
        .where('id', id)\
        .update(params)


@login_required
def delete(request, id):
    Post.where('id', id).delete()

    return redirect('/mypage/')
