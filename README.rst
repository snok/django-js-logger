========================
Django Javascript Logger
========================

.. image:: https://img.shields.io/pypi/v/django-js-logger.svg
    :target: https://pypi.org/project/django-js-logger/

.. image:: https://img.shields.io/pypi/pyversions/django-js-logger.svg
    :target: https://pypi.org/project/django-js-logger/

.. image:: https://img.shields.io/pypi/djversions/django-js-logger.svg
    :target: https://pypi.python.org/pypi/django-js-logger

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://pypi.org/project/django-swagger-tester/

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    :target: https://github.com/pre-commit/pre-commit

Simple Django app for logging Javascript's ``console.log`` logs to Django.

Useful for catching Javascript errors that are not logged by Django natively and would otherwise only be logged to the client's console.

The structure is very simple. The app simply has an API that receives logs from the client. Because of this, you likely want to avoid running this in production.

.. image:: docs/img/chart.png
  :width: 600
  :align: center
  :alt: Flowchart

If you want to implement this, and need to add custom headers or other functionality, please commit an issue. Otherwise, this currently does exactly what I need it to do.

Quick start
-----------

1. Add "js_logger" to your INSTALLED_APPS settings::

    INSTALLED_APPS = [
        ...
        'js_logger',
    ]

2. Include the packages URLconf in your project urls.py like this::

    path('js-logs/', include('js_logger.urls')),

3. Add the required static file to your project by running ``manage.py collectstatic``, or by manually adding the following code to ``<your-templates-folder>/js-logging/js-logging.html``::

    <script type="text/javascript">
        function post(type, msg) {
            let headers;
            if (window.jsLoggerHeader) {
                headers = window.jsLoggerHeader;
            } else {
                headers = {'Content-Type': 'application/json'};
            }
            fetch('/js-logs/', {method: 'POST', headers: headers, body: JSON.stringify({'type': type, 'msg': msg})});
        }

        window.addEventListener('error', (event) => {
            post('error', event.message);
        });

        console._overwritten = console.log;
        console.log = function (log) {
            post('info', log);
            console._overwritten(log);
        }
    </script>


4. Include the template where you wish::

    <head>
    ...
    {% include "js-logging/js-logging.html" %}
    ...
    </head>


5. Add ``console.log`` as a logger in your logging configuration::

    'console.log': {
        'level': 'INFO',
        ...
    },

Note: This package will log all `console.log` calls in your frontend as ``INFO`` logs, and will log javascript errors as ``ERROR`` logs.
