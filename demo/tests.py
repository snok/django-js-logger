from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from rest_framework.test import APISimpleTestCase
from selenium.webdriver import Chrome

driver = Chrome()


class TestLogging(StaticLiveServerTestCase):

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
        with self.assertLogs(level='ERROR') as log:
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


class TestApi(APISimpleTestCase):

    def test_bad_data(self):
        """
        Make sure we're logging a warning when the "pipeline" fails.
        """
        with self.assertLogs(level='WARNING') as log:
            self.client.post('/js-logs/', data={'test': 'bad data'})
            assert 'Received bad data' in log.output[0]
            assert len(log.output) == 1  # <-- this was an issue - everything was logging twice
