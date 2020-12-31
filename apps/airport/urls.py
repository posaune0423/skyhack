from django.urls import path
from apps.airport import views

app_name = 'airport'
urlpatterns = [
    path('<int:pk>', views.show),
    path('search/', views.Search.as_view()),
]
