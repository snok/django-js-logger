from django.urls import path

from js_logger.views import JsLoggerApi

urlpatterns = [
    path('', JsLoggerApi.as_view(), name='js-logging-api'),
]
