from django.shortcuts import render

from apps.orater.user import User
from apps.orater.post import Post


def show(request, id):
    user = User.find(id)
    posts = Post\
        .where('author_id', id)\
        .order_by('pub_date', 'desc')\
        .get()


    return render(request, 'users/show.html', {'user': user, 'posts': posts})