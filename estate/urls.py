from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.conf import settings
# from django.conf.urls.static import static
from estateapp import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^success/', views.success, name='success'),
    url(r'^service/', views.service, name='service'),
    url(r'^house/info/', views.PropertyView.as_view(), name='house'),
    url(r'^form/photo_upload/', views.photo_upload, name='photo_upload'),
    path('admin/', admin.site.urls),

]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
