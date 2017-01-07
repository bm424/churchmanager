from django.conf.urls import url, include
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
    url(r'^news/$', views.NewsList.as_view(), name='news-list'),
    url(r'^news/(?P<pk>[\d]+)/$', views.NewsDetail.as_view(), name='news-detail'),
    url(r'^village-churches/$', views.VillageChurchList.as_view(), name='village-list'),
    url(r'^town-churches/$', views.TownChurchList.as_view(), name='town-list'),
    url(r'^churches/$', views.VillageChurchList.as_view(), name='church-list'),
    url(r'^churches/(?P<slug>[-\w]+)/$', views.ChurchDetail.as_view(), name='church-detail'),
    url(r'^$', RedirectView.as_view(url='news/'), name='home'),
]
