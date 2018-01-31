from django.conf.urls import url
from . import views
from app.views import list


urlpatterns = [
    url(r'^search/', views.search),
    url(r'^selections/', views.selections),
    url(r'^index/', views.home),
    #url(r'^', views.home),
    url(r'^db_update/$', list, name='list'),
    url(r'^edit/kartochka_kompanii/(?P<id>\w+)/$', views.edit_kartochka, name='edit/kartochka_kompanii'),
    url(r'^edit/korp_kontrol/(?P<id>\w+)/$', views.edit_korp_kontrol, name='edit/korp_kontrol'),
    url(r'^edit/raskrytie/(?P<id>\w+)/$', views.edit_raskrytie, name='edit/raskrytie'),
    url(r'^edit/administrativka/(?P<id>\w+)/$', views.edit_administrativka, name='edit/administrativka'),
    url(r'^edit/vzaimodeystvie/(?P<id>\w+)/$', views.edit_vzaimodeystvie, name='edit/vzaimodeystvie')
]
