from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^bizdir/', include('bizdir.foo.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),

    (r'^category/(?P<slug>.*).html$', 'catalog.views.show_category'),
    (r'^host/(?P<slug>.*).html$', 'catalog.views.show_host'),
    (r'^hosts/(?P<slug>.*).html$', 'catalog.views.show_category'),
    (r'^hosts.html$', 'catalog.views.show_categories'),

    (r'^leaderboard.html$', 'catalog.views.leaderboard'),
    (r'^visit/(?P<slug>.*).html$', 'catalog.views.visit'),

    (r'^comment/helpful/(?P<id>.*).html$', 'catalog.views.helpful'),
    (r'^comment/report/(?P<id>.*).html$', 'catalog.views.report'),

    (r'^$|index.html$', 'main.views.index'),

    (r'^(?P<slug>(.*)).html', 'main.views.get_page'),
)
