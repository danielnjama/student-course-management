from django.contrib import admin
# from django.contrib.auth import views as auth_views

from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
# from django.views.generic import RedirectView


admin.site.site_header="Dtech Coding Hub"
admin.site.site_title="Dtech Coding Hub"
admin.site.index_title="Dtech Coding Hub"

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('',include("home.urls")),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns= urlpatterns+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)