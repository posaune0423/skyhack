from django.contrib.auth.decorators import login_required
from django.urls import path

import apps.user.views
import apps.review.views

urlpatterns = [
    path('profile/', login_required(apps.user.views.Update.as_view())),
    # path('delete/<int:pk>', login_required(apps.review.views.delete)),
    path('', login_required(apps.user.views.index)),
]
