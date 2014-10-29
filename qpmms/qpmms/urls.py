from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('qpscsmas.views',
    # Examples:
    # url(r'^$', 'qpmms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^dashboard/', 'qpscsmas.views.dashboard',name='dashboard'),
    # url(r'^login/','qpscsmas.views.login',name='login'),
    url(r'^$','login'),
    url(r'^login','login'),
    url(r'^dashboard','dashboard'),
    url(r'^registeremployee','registeremployee'),
    url(r'^viewemployee','viewemployee'),
    url(r'^registercompanies','registercompanies'),
    url(r'^viewcompanies','viewcompanies'),
    url(r'^registerdevices','registerdevices'),
    url(r'^viewdevices','viewdevices'),
)