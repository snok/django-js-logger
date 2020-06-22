from django.urls import path

from js_logger.views import JsLoggerApi

urlpatterns = [
    path('', JsLoggerApi.as_view(), name='django_js_logger-api'),
]
