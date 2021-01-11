from django.conf.urls import url
from . import views
from django.urls import path

app_name ='mysite'

urlpatterns = [
   # path('', views.index , name='index'),
   path('', views.Index.as_view(), name='index'),
]