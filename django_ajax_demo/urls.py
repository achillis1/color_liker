from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_ajax_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^color_liker/', include('color_liker.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
