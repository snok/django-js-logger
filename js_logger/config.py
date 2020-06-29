import logging
from typing import Callable

from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured


def get_logger(level: str, logger_name: str) -> Callable:
    """
    Return logger.

    :param level: log level
    :param logger_name: logger name
    :return: logger
    """
    if level == 'DEBUG':
        return logging.getLogger(logger_name).debug
    elif level == 'INFO':
        return logging.getLogger(logger_name).info
    elif level == 'WARNING':
        return logging.getLogger(logger_name).warning
    elif level == 'ERROR':
        return logging.getLogger(logger_name).error
    elif level == 'EXCEPTION':
        return logging.getLogger(logger_name).exception
    elif level == 'CRITICAL':
        return logging.getLogger(logger_name).critical
    else:
        raise ImproperlyConfigured(f'The log level for the `{logger_name}` logger was set as `{level}` ' f'which is not a valid log level.')


class Settings(object):
    """
    Load package settings.
    """

    def __init__(self) -> None:
        """
        Set package setting attributes.
        """
        self.CONSOLE_LOG_LEVEL = 'INFO'
        self.CONSOLE_ERROR_LEVEL = 'WARNING'

        if not hasattr(django_settings, 'JS_LOGGER') or not django_settings.JS_LOGGER:
            return

        package_settings = django_settings.JS_LOGGER
        for setting, value in package_settings.items():
            if hasattr(self, setting):
                setattr(self, setting, value)
            else:
                raise ImproperlyConfigured(f'`{setting}` is not a valid setting for the django-js-logger module')

        self.CONSOLE_LOG_LOGGER = get_logger(level=self.CONSOLE_LOG_LEVEL, logger_name='console_logs')
        self.CONSOLE_ERROR_LOGGER = get_logger(level=self.CONSOLE_ERROR_LEVEL, logger_name='console_errors')


settings = Settings()
