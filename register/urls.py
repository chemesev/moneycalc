from django.conf.urls import url, include

from . import views

app_name = 'registration'
urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/signup/$', views.register_user, name='sign_up')
]
