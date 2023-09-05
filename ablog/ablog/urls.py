from django.contrib import admin
from django.urls import path,include

from django.conf import settings #for media
from django.conf.urls.static import static  #for media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
    path('members/',include('django.contrib.auth.urls')), # django.contrib.auth.urls = Django library for auth. note: this should be listed first before the actual path for your app.
    path('members/', include('members.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #for media 
