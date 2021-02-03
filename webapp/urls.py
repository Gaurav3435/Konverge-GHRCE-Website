from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
urlpatterns = [
    path('',views.start_ ),
    path('contact/',views.contact_form),
    path('blog/<int:myid>',views.blog_detail),
    path('research/<int:myid>',views.blog_detail),
    path('project/<int:myid>',views.blog_detail),
    path('r_project/<int:myid>',views.blog_detail),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]
urlpatterns+=staticfiles_urlpatterns()