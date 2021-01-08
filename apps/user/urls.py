from django.contrib.auth.decorators import login_required
from django.urls import path

import apps.user.views

urlpatterns = [
    path('<int:pk>', login_required(apps.user.views.show))
]
