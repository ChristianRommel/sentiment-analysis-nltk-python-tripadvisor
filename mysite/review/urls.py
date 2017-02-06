from django.conf.urls import url

from . import views

urlpatterns = [
    # 1: Path 2: View_Name 3:Name
    url(r'^$', views.index, name='index'),
    url(r'^reviews/$', views.reviews, name='reviews'),
    url(r'^evaluation/$', views.evaluation, name='evaluation'),
]
