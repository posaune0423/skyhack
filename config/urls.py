from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.conf.urls.static import static

import apps.airport.views
import apps.user.views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('home/', apps.airport.views.Index.as_view()),
                  path('login/', LoginView.as_view(template_name='login.html')),
                  path('logout/', LogoutView.as_view()),
                  path('signup/', apps.user.views.Create.as_view()),
                  path('airports/', include('apps.airport.urls')),
                  path('mypage/', include('apps.mypage.urls')),
                  path('reviews/', include('apps.review.urls')),
                  path('', apps.airport.views.top),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
