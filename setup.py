from setuptools import find_packages, setup

from js_logger import __author__, __version__

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as changelog_file:
    changelog = changelog_file.read()

setup(
    name='django-js-logger',
    version=__version__,
    description='Javascript logging for Django.',
    py_modules=['js_logger'],
    packages=find_packages(),
    include_package_data=True,
    long_description=readme + '\n\n' + changelog,
    license='BSD',
    author=__author__,
    author_email='sondrelg@live.no',
    url='https://github.com/sondrelg/django-js-logger',
    download_url='https://pypi.python.org/pypi/django-js-logger',
    install_requires=['djangorestframework', 'django'],
    keywords=['console', 'log', 'logging', 'javascript', 'django'],
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Documentation',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: Unit',
    ],
)
