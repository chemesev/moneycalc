from django.conf.urls import url
from . import views

app_name = 'calculator'
urlpatterns = [
    url(r'^$', views.budget_edit, name='index'),
    url(r'^base/$', views.base)
]
