from django.conf.urls import include, url
from . import views
from django.urls import path

# app_name ='mysite'

# urlpatterns = [
#    # path('', views.index , name='index'),
#    path('', views.Index.as_view(), name='index'),
# ]

# urlpatterns = [
#    url(r"^accounts/", include("django.contrib.auth.urls")),
#    url(r'^', views.Index.as_view(), name='index'),
# ]


urlpatterns = [
   #  path('', views.indexvch, name='index'),
   path('', views.Index.as_view(), name='index'),
]