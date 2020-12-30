from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.posts import views

app_name = 'posts'
urlpatterns = [
    path('', login_required(views.Index.as_view())),
    path('create/', login_required(views.Create.as_view())),
    path('<int:pk>/update', login_required(views.Update.as_view())),
    path('<int:pk>/delete', views.delete),
    path('<int:pk>', login_required(views.Show.as_view())),
]
