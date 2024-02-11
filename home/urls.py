from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .views import*
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   path('',home,name='home'),
   path('add-blog/',add_blog,name='add_blog'),
   path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
   path('see_blog/',see_blog,name='see_blog'),
   path('blog-delete/<id>',blog_delete,name='blog_delete'),
   path('blog-update/<slug>/', blog_update, name="blog_update"),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
urlpatterns = urlpatterns + staticfiles_urlpatterns()