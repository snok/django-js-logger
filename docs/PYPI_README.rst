========================
Django Javascript Logger
========================

.. image:: https://img.shields.io/pypi/v/django-js-logger.svg
    :target: https://pypi.org/project/django-js-logger/

.. image:: https://img.shields.io/pypi/pyversions/django-js-logger.svg
    :target: https://pypi.org/project/django-js-logger/

.. image:: https://img.shields.io/pypi/djversions/django-js-logger.svg
    :target: https://pypi.python.org/pypi/django-js-logger

.. image:: https://codecov.io/gh/sondrelg/django-js-logger/branch/master/graph/badge.svg
    :alt: Code coverage
    :target: https://codecov.io/gh/sondrelg/django-js-logger/

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    :alt: Pre-commit enabled
    :target: https://github.com/pre-commit/pre-commit

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :alt: Code style black
    :target: https://pypi.org/project/django-swagger-tester/

.. image:: http://www.mypy-lang.org/static/mypy_badge.svg
    :alt: Checked with mypy
    :target: http://mypy-lang.org/

|

This is a very simple Django app for forwarding console logs and console errors to dedicated Django loggers.

Useful for catching Javascript errors that are not logged by Django natively and would otherwise only be logged to the client's console. Can be particularly useful if you have JavaScript running on top of our server-side rendered views.

The app works by posting *all relevant events* to an internal Django API, which logs them to one of two loggers. Not sure what impact this has on an apps performance, but it likely should not run anywhere near performance-sensitive production environments. Primarily this is intended to be a debugging aid.

A flowchart of the app's structure looks something like this:

.. image:: docs/img/flowchart.png

The package is open to contributions.

Installation
------------

Installing with pip::

    pip install django-js-logger

Installing with poetry::

    poetry add django-js-logger

Quick start
-----------

1. Add ``django_js_logger`` to your INSTALLED_APPS settings::

    INSTALLED_APPS = [
        ...
        'django_js_logger',
    ]

2. Include the packages URLconf in your project urls.py like this::

    path('js-logs/', include('django_js_logger.urls')),

3. Optionally, specify your logging preferences by adding ``JS_LOGGER`` to your settings::

    JS_LOGGER = {
        'CONSOLE_LOG_LEVEL': 'INFO',
        'CONSOLE_ERROR_LEVEL': 'WARNING'
    }

4. Add the required static file to your project by running ``manage.py collectstatic``. This should add a folder, ``django_js_logger`` with the file ``logger.js``. If this is not the case, you can copy the file manually from the demo project above.

5. Import ``logger.js`` in the views you wish to log from by adding a JS import to your templates::

    <script src="static/django_js_logger/logger.js"></script>
