from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.views.generic import ArchiveIndexView
from blog.models import Blog
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'siliqua.views.home', name='home'),
    # url(r'^siliqua/', include('siliqua.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


        (r'^$', 'blog.views.index'),
    url(
        r'^blog/view/(?P<slug>[^\.]+).html',
        'blog.views.view_post',
        name='view_blog_post'),
    url(
        r'^blog/category/(?P<slug>[^\.]+).html',
        'blog.views.view_categoria',
        name='view_blog_categoria'),

        (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    url(r'^$', ArchiveIndexView.as_view(model=Blog, date_field='posted')),
)


