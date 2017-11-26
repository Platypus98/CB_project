from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search/', views.search),
    url(r'^selections/', views.selections),
    url(r'^index/', views.home),
    url(r'^edit/kartochka_kompanii/(?P<id>\w+)/$', views.edit_kartochka, name='edit/kartochka_kompanii'),
    url(r'^edit/korp_kontrol/(?P<id>\w+)/$', views.edit_korp_kontrol, name='edit/korp_kontrol')
]
