from django.urls import path

from django_js_logger.views import JsLoggerApi

urlpatterns = [
    path('', JsLoggerApi.as_view(), name='django_js_logger-api'),
]
