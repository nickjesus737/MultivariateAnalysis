from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create-proyecto/$', views.create_proyecto),
    url(r'^create-estudio/$', views.create_estudio),
    url(r'^ejecutar-estudio/(?P<id>[0-9])/$', views.ejecutar_estudio),
]