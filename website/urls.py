from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'woof/roster', views.woofroster, name='woofroster'),
    url(r'woof/about', views.woofabout, name='woofabout'),
    url(r'woof/gallery', views.woofgallery, name='woofgallery'),
    url(r'woof/contactus', views.woofcontactus, name='woofcontactus'),
    url(r'bark/about', views.barkabout, name='barkabout'),
    url(r'bark/roster', views.barkroster, name='barkroster'),
    url(r'bark/gallery', views.barkgallery, name='barkgallery'),
    url(r'bark/contactus', views.barkcontactus, name='barkcontactus'),
    url(r'monstars/about', views.monstarsabout, name='monstarsabout'),
    url(r'monstars/roster', views.monstarsroster, name='monstarsroster'),
    url(r'monstars/gallery', views.monstarsgallery, name='monstarsgallery'),
    url(r'monstars/contactus', views.monstarscontactus, name='monstarscontactus'),
]