from django.conf.urls import url
from django.contrib import admin
from . import view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.home),
    url(r'^signin$', view.signin),
    url(r'^signin_form$', view.signin_form),
]