from django.contrib.auth.decorators import login_required
from django.urls import path

import apps.review.views

app_name = 'review'
urlpatterns = [
    path('<int:pk>/edit', login_required(apps.review.views.Update.as_view()), name='update'),
    path('create/', login_required(apps.review.views.Create.as_view()), name='create'),
    path('<int:pk>/delete', apps.review.views.delete, name='delete'),
]
