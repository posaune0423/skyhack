from django.contrib.auth.decorators import login_required
from django.urls import path

import apps.review.views

urlpatterns = [
    path('<int:pk>/edit', login_required(apps.review.views.Update.as_view())),
    path('create/', login_required(apps.review.views.Create.as_view())),
    path('<int:pk>/delete', apps.review.views.delete),
]
