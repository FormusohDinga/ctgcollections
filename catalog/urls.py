from django.conf.urls import url

from .views import (DvdList, DvdCreate,DvdUpdate,DvdDelete, dvd_detail)

urlpatterns = [
    url(r'^$',
        DvdList.as_view(),
        name='catalog_dvd_urls'),
    url(r'^dvd/create/$',
        DvdCreate.as_view(),
        name='dvd_create'),
    url(r'^dvd/(?P<slug>[\w\-]+)/$',
        dvd_detail,
        name='dvd_detail'),
    url(r'^dvd/(?P<slug>[\w\-]+)/update/$',
        DvdUpdate.as_view(),
        name='dvd_update'),
    url(r'^dvd/(?P<slug>[\w\-]+)/delete/$',
        DvdDelete.as_view(),
        name='dvd_delete'),
        ]
