from django.contrib.auth.decorators import login_required
from django.urls import path

import apps.review.views

urlpatterns = [
    # path('<int:pk>/edit', login_required(apps.review.views.Update.as_view())),
    # path('create/', login_required(apps.review.views.Create.as_view())),
    path('<int:id>/edit', apps.review.views.update),
    path('create/', apps.review.views.create),
    path('<int:id>/delete', apps.review.views.delete),
]
