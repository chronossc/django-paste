from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',

    (r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^admin_media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':'/home/felipe.py/2.5/lib/python2.5/site-packages/django/contrib/admin/media/' }),
    (r'^admin/', include(admin.site.urls)),
    (r'^',include('dpaste.urls')),

)
