from django.urls import path

from apps.posts import views

app_name = 'posts'
urlpatterns = [
    path('', views.top)
]