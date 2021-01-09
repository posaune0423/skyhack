from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include


import apps.airport.views
import apps.user.views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('signup/', apps.user.views.Create.as_view()),
                  path('login/', LoginView.as_view(template_name='login.html')),
                  path('logout/', LogoutView.as_view()),
                  path('home/', apps.airport.views.Index.as_view()),
                  path('airports/', include('apps.airport.urls')),
                  path('reviews/', include('apps.review.urls')),
                  path('mypage/', include('apps.mypage.urls')),
                  path('users/', include('apps.user.urls')),
                  path('', apps.airport.views.top),
              ]