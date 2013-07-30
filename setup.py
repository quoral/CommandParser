try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Command Parser',
    'author': 'Karl Johan Krantz',
    'url': 'http://github.com/schwomp/CommandParser',
    'author_email': 'schwomp@gmail.com',
    'version': '0.0.0',
    'install_requires': ['nose'],
    'packages': ['cmdparse'],
    'name': 'CommandParser'
}

setup(**config)