.. _contributing:

************
Contributing
************

This package is open to contributions. To contribute, please follow these steps:

1. Fork the upstream django-js-logger repository into a personal account.
2. Install poetry_, and install dev dependencies using ``poetry install``
3. Install pre-commit_ (for project linting) by running ``pre-commit install``.
4. Create a new branch for you changes
5. Push the topic branch to your personal fork.
6. Create a pull request to the django-js-logger repository with a detailed explanation of your changes.

.. _poetry: https://python-poetry.org/
.. _pre-commit: https://pre-commit.com/

*********************
Pushing code coverage
*********************

Since we're using Selenium for testing, we've not tried to automate the codecov upload.

To upload codecov, test locally using ``coverage run manage.py test``, then upload coverage by running::

    bash <(curl -s https://codecov.io/bash) -t <codecov token> -f .coverage
