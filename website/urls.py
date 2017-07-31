from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'woof', views.woofabout, name='woofabout'),
    url(r'woof', views.woofroster, name='woofroster'),
    #url(r'woof', views.woofgallery, name='woofgallery'),
    #url(r'woof', views.woofcontactus, name='woofcontactus'),
    #url(r'bark', views.barkabout, name='barkabout'),
    #url(r'bark', views.barkroster, name='barkroster'),
    #url(r'bark', views.barkgallery, name='barkgallery'),
    #url(r'bark', views.barkcontactus, name='barkcontactus'),
    #url(r'monstars', views.monstarsabout, name='monstarsabout'),
    #url(r'monstars', views.monstarsroster, name='monstarsroster'),
    #url(r'monstars', views.monstarsgallery, name='monstarsgallery'),
    #url(r'monstars', views.monstarscontactus, name='monstarscontactus'),
]