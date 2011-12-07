from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    (r'^$', views.index),
    (r'^search/$',views.search),
    (r'^song/(.{1,30})', views.song),
    

)
