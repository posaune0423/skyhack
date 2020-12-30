from django.urls import path

import apps.users.views
import apps.posts.views

urlpatterns = [
    path('create/', apps.posts.views.create),
    path('delete/<int:id>', apps.posts.views.delete),
    path('update/<int:id>', apps.posts.views.update),
    path('', apps.users.views.index),
]
