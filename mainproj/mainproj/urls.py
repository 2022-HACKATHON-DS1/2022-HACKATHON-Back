from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mapapp import views as mapapp_views
from mainapp import views as main_views
from accounts import views as accounts_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('detail/<int:post_id>', main_views.detail, name="detail"),
    path('mypage/', main_views.mypage, name='mypage'),
    path('newpost/', main_views.postformcreate, name='newpost'),
    path('map/', mapapp_views.map, name='map'),
    path('event/', main_views.event, name='event'),
    path('reward/', main_views.reward, name='reward'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)