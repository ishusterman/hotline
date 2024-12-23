from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth import views as auth_views


from django.conf.urls import url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
                  #url(r'^accounts/login/$', auth_views.login),
                  url(r'^request/', include('app_hotline.urls')),
                  #url(r'^view/', include('app_hotline.urls')),
                  #url(r'^auth/user/$', auth_views.login),
                  url(r'^', admin.site.urls),
                  url(r'^select2/', include('select2.urls')),
                  url(r'^index/', include('app_hotline.urls')),
                  # url(r'^logoff/', views.logoff, name='logoff'),
                  # url(r'^edit/$', views.edit, name='edit'),


              ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)


