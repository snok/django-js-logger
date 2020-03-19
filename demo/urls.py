from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('js-logs/', include('js_logger.urls')),
]
