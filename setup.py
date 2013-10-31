import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

requires = [
    'pyramid_chameleon',
    'pyramid',
    'deform',
    'nose'
]

setup(
    version='0.1',
    description='deform demo',
    install_requires=requires,
    author='Pete Graham',
    author_email='pete@lostpropertyhq.com',
    url='',
    packages=find_packages(),
)
