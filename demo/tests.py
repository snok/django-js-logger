from unittest.mock import patch

from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.exceptions import ImproperlyConfigured
from django.test import SimpleTestCase

from django_js_logger.config import get_logger, Settings
from selenium.webdriver import Chrome


class TestLogging(StaticLiveServerTestCase):
    driver = Chrome()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = Chrome()
        cls.selenium.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_error_logging(self):
        """
        Verify that a triggered error results in a django error-log.
        """
        self.selenium.get(self.live_server_url)
        button = self.selenium.find_element_by_id('error')
        with self.assertLogs(level='WARNING') as log:
            button.click()
            self.selenium.implicitly_wait(2)  # <-- race condition
            assert 'SyntaxError: Missing initializer in const declaration' in log.output[0]

    def test_console_logging(self):
        """
        Verify that a javascript console.log() triggers a django info-log.
        """
        self.selenium.get(self.live_server_url)
        button = self.selenium.find_element_by_id('info')
        with self.assertLogs(level='INFO') as log:
            button.click()
            self.selenium.implicitly_wait(2)  # <-- race condition
            assert 'test' in log.output[0]


class TestConfig(SimpleTestCase):
    def test_get_logger(self):
        import logging

        self.assertEqual(get_logger('DEBUG', 'test'), logging.getLogger('test').debug)
        self.assertEqual(get_logger('INFO', 'test'), logging.getLogger('test').info)
        self.assertEqual(get_logger('WARNING', 'test'), logging.getLogger('test').warning)
        self.assertEqual(get_logger('ERROR', 'test'), logging.getLogger('test').error)
        self.assertEqual(get_logger('EXCEPTION', 'test'), logging.getLogger('test').exception)
        self.assertEqual(get_logger('CRITICAL', 'test'), logging.getLogger('test').critical)
        for i in ['', 's', 0, [], {}, None]:
            with self.assertRaisesMessage(
                ImproperlyConfigured,
                expected_message=f'The log level for the `test` logger was set as `{i}` which is not a valid log level.',
            ):
                get_logger(i, 'test')

    valid_log_levels = [
        'DEBUG',
        'INFO',
        'WARNING',
        'ERROR',
        'EXCEPTION',
        'CRITICAL',
    ]

    @patch.object(settings, 'JS_LOGGER', None)
    def test_missing_settings(self):
        self.assertEqual(Settings().CONSOLE_LOG_LEVEL, 'INFO')
        self.assertEqual(Settings().CONSOLE_ERROR_LEVEL, 'WARNING')

    def test_set_log_levels(self):
        for level in self.valid_log_levels:
            with patch.object(settings, 'JS_LOGGER', {'CONSOLE_LOG_LEVEL': level, 'CONSOLE_ERROR_LEVEL': level}):
                js_settings = Settings()
                self.assertEqual(js_settings.CONSOLE_LOG_LEVEL, level)
                self.assertEqual(js_settings.CONSOLE_ERROR_LEVEL, level)

    @patch.object(settings, 'JS_LOGGER', {'bad setting': ''})
    def test_invalid_setting(self):
        with self.assertRaisesMessage(
            ImproperlyConfigured, expected_message=f'`bad setting` is not a valid setting for the django-js-logger module'
        ):
            Settings()
