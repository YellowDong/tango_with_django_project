from django.conf.urls import url
from Rango import views

app_name = 'rango'
urlpatterns = [
    url("^$", views.index, name='index'),
    url("^about/", views.about, name='about'),
    url("^category/(?P<category_name_url>[\w\-]+)/$", views.show_category, name='category'),
    url("^add_category/", views.add_category, name='add_category')
]