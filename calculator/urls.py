from django.conf.urls import url
from . import views

app_name = 'calculator'
urlpatterns = [
    url(r'^$', views.budget_edit, name='budget_edit'),
    url(r'^base/$', views.base)
]
