from __future__ import unicode_literals
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from apps.posts.models import Post
from apps.users.forms import SignUpForm
from apps.users.models import User


class Create(CreateView):
    form_class = SignUpForm
    model = User
    template_name = 'signup.html'
    success_url = '/login/'

    def form_valid(self, form):
        user = form.save()  # save form info
        login(self.request, user)  # authorise
        self.object = user
        return HttpResponseRedirect(self.get_success_url())


class Update(UpdateView):
    model = User
    fields = ('thumbnail', 'name', 'email', 'bio')
    template_name = 'mypage/profile.html'
    success_url = '/mypage/'

    def get_object(self):
        return self.request.user


def index(request):
    queryset = Post.objects \
    .filter(author=request.user.id) \
    .order_by('-created_at')[:5]

    return render(request, 'mypage/index.html', {'posts': queryset})


def show(request, pk):
    user = User.objects.get(pk=pk)
    posts = Post.objects \
    .filter(author=user.id) \
    .order_by('-created_at')[:5]

    return render(request, 'users/show.html', {'selected_user': user, 'posts': posts})


def create(request):
    return render(request, 'mypage/create.html')
