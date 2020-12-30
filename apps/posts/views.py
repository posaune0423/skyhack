from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from apps.posts.models import Post
from apps.posts.forms import PostForm


class Index(ListView):
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('q')

        if q_word:
            object_list = Post.objects \
                              .filter(Q(country__icontains=q_word)) \
                              .order_by('-created_at')[:6]
        else:
            object_list = Post.objects \
                              .filter(created_at__lte=timezone.now()) \
                              .order_by('-created_at')[:6]
        return object_list


class Search(ListView):
    template_name = 'search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('q')

        if q_word:
            object_list = Post.objects \
                              .filter(Q(title__icontains=q_word) | Q(author__name__icontains=q_word)) \
                              .order_by('-created_at')[:6]
        else:
            object_list = None
        return object_list


class Show(DetailView):
    model = Post
    template_name = 'posts/show.html'
    context_object_name = 'post'


class Create(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'mypage/create.html'
    success_url = '/mypage/'


class Update(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'mypage/edit.html'


def top(request):
    return render(request, 'index.html')


@login_required
def delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    if (request.user.id != post.author_id):
        return redirect('/mypage/')

    post.delete()
    return redirect('/mypage/')
