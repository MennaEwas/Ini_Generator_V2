from django.urls import path
from . import views 

app_name = 'Oadmin'
#URLConf
urlpatterns = [
    path('', views.admin_view_selectg.as_view(), name = 'home'),
]