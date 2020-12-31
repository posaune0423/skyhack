from django.contrib.auth.decorators import login_required
from django.urls import path

import apps.user.views
import apps.review.views

urlpatterns = [
    path('profile/', login_required(apps.user.views.Update.as_view())),
    path('', login_required(apps.user.views.index)),
]
