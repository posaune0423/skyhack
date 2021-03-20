from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.airport import views

app_name = 'airport'
urlpatterns = [
    path('<int:pk>', views.show, name='show'),
    path('search/', login_required(views.Search.as_view()), name='search'),
]
