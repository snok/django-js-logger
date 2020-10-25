from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index),
    path('js-logs/', include('django_js_logger.urls')),
]
