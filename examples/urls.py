from django.conf.urls.defaults import patterns, include, url
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from blogpost.resources import (BlogPostResource, CommentResource,
        BasicBlogPostResource)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'examples.views.home', name='home'),
    # url(r'^examples/', include('examples.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blogpost.urls')),
    url(r'^basic$',
        ListOrCreateModelView.as_view(resource=BasicBlogPostResource),
        name='basic-blog-posts'),
    url(r'^(?P<pk>[^/]+)/$',
        InstanceModelView.as_view(resource=BasicBlogPostResource)),
)
