from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

import apps.posts.views
import apps.users.views
from config import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('login/', LoginView.as_view(template_name='login.html'), name='login'),
                  path('logout/', LogoutView.as_view()),
                  path('signup/', apps.users.views.Create.as_view(), name='signup'),
                  path('posts/', include('apps.posts.urls')),
                  path('search/', apps.posts.views.Search.as_view()),
                  path('users/<int:pk>', apps.users.views.show),
                  path('mypage/', include('apps.mypage.urls')),
                  path('', apps.posts.views.top)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
