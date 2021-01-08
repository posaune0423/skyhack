from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView

from apps.review.models import Review
from apps.user.forms import SignUpForm
from apps.user.models import User


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
    fields = ('thumbnail', 'username', 'email', 'bio')
    template_name = 'mypage/../../templates/user/edit.html'
    success_url = '/mypage/'

    def get_object(self):
        return self.request.user


@login_required
def index(request):
    is_mypage = True
    reviews = Review.objects \
                  .filter(author=request.user.id) \
                  .order_by('-created_at')[:4]

    return render(request, 'user/show.html', {'reviews': reviews, 'is_mypage': is_mypage})


@login_required
def show(request, pk):
    if (request.user.id == pk):
        return redirect('/mypage/')
    user = User.objects.get(pk=pk)
    reviews = Review.objects \
                  .filter(author=user.id) \
                  .order_by('-created_at')[:5]

    return render(request, 'user/show.html', {'selected_user': user, 'reviews': reviews})
