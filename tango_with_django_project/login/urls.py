from . import views
from django.conf.urls import url
app_name = 'user'
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^confirm/', views.confirm, name='confirm'),
]