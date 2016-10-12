from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from mysite import views as mysite_views
from mysite.views import hello, current_datetime, hours_ahead, request_info

from django.views.generic import list
from books.models import Publisher
from hosttracker import views as hosttracker_views

from django.contrib.auth.views import login, logout

from register import register

import sys
sys.path.append("..")
from books import views as books_views
from contact import views as contact_views
from hosttracker import urls as hosttracker_urls


publisher_info = {
    'queryset': Publisher.objects.all(),
    'template_name': 'publisher_list_page.html',
}

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    ('^time/plus/(\d{1,2})/$', hours_ahead),
    ('^request_info/$', request_info),
    (r'^search-form/$', books_views.search_form),
    (r'^search/$', books_views.search),
    url(r'^contact/$', contact_views.contact),
    #(r'^debuginfo/$', mysite.views.debug),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hosttracker/', include(hosttracker_urls)),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url('^test/$', hello),
    #url(r'^articles/(\d{4})/$', mysite_views.year_archive),
    #url(r'^articles/(\d{4})/(\d{2})/$', mysite_views.month_archive),
    url(r'^articles/(?P<year>\d{4})/$', mysite_views.year_archive),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', mysite_views.month_archive),

    url(r'^foo/$', mysite_views.foobar_view, {'template_name': 'template1.html'}),
    url(r'^bar/$', mysite_views.foobar_view, {'template_name': 'template2.html'}),

    url(r'^mydata/birthday/$', mysite_views.views_myview, {'month': 'jan', 'day': '13'}),
    url(r'^mydata/(?P<month>\w{3})/(?P<day>\d\d)/$', mysite_views.views_myview),

    #url(r'^events/$', views.object_list, {'model': models.Event}),
    #url(r'^blog/entries/$', views.object_list, {'model': models.BlogEntry}),

    url(r'^publishers/$', list.View, publisher_info),
    url(r'^my_image/$', mysite_views.my_image),
    url(r'^unruly_passengers_csv/$', mysite_views.unruly_passengers_csv),
    url(r'^hello_pdf/$', mysite_views.hello_pdf),
    url(r'^set_color/$', mysite_views.set_color),
    url(r'^show_color/$', mysite_views.show_color),

    url(r'^accounts/login/$', login, {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/register/$', register),
    url(r'^test_icon/$', mysite_views.test_icon),
)
