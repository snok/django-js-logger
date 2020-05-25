from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from js_logger.config import settings

loggers = {
    'console_log': settings.CONSOLE_LOG_LOGGER,
    'console_error': settings.CONSOLE_ERROR_LOGGER,
}


class JsLoggerApi(APIView):
    @staticmethod
    def post(request: Request) -> Response:
        """
        Receives logs from the client, which we re-log with a python logger.
        """
        if 'msg' in request.data and 'type' in request.data:
            loggers[request.data['type']](msg=request.data['msg'])
        return Response(status=HTTP_204_NO_CONTENT)
