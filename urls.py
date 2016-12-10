from django.conf.urls import url, include
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
    url(r'^churches/$', views.ChurchList.as_view(), name='church-list'),
    url(r'^churches/(?P<slug>[-\w]+)/$', views.ChurchDetail.as_view(), name='church-detail'),
    url(r'^$', RedirectView.as_view(url='churches/'), name='home')
]
