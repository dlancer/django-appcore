import os
from setuptools import setup, find_packages
from appcore import get_version as get_package_version

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
REQUIREMENTS = os.path.join(os.path.dirname(__file__), 'requirements.txt')
reqs = open(REQUIREMENTS).read().splitlines()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-appcore',
    version=get_package_version(),
    packages=find_packages(),
    install_requires=reqs,
    license='BSD',
    include_package_data=True,
    description='Reusable useful tools for Django 1.5+ application programming.',
    long_description=README,
    url='https://github.com/dlancer/django-appcore',
    author='dlancer',
    author_email='dmdpost@gmail.com',
    maintainer='dlancer',
    maintainer_email='dmdpost@gmail.com',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Development Status :: 2 - Pre-Alpha',
    ],
)
