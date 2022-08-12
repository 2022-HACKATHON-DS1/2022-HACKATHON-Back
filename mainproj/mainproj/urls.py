from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mapapp import views as mapapp_views
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detail/<int:post_id>', views.detail, name="detail"),
    path('mypage/', views.mypage, name='mypage'),
    path('newpost/', views.postformcreate, name='newpost')
    path('map/',mapapp_views.map, name='map'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)