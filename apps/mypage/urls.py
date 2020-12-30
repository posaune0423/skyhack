from django.contrib.auth.decorators import login_required
from django.urls import path

import apps.users.views
import apps.posts.views

urlpatterns = [
    path('profile/', login_required(apps.users.views.Update.as_view())),
    path('delete/<int:pk>', login_required(apps.posts.views.delete)),
    path('', login_required(apps.users.views.index)),
]
