from setuptools import setup, find_packages
import os

# The version of the wrapped library is the starting point for the
# version number of the python package.
# In bugfix releases of the python package, add a '-' suffix and an
# incrementing integer.
# For example, a packaging bugfix release version 1.4.4 of the
# js.jquery package would be version 1.4.4-1 .

version = '1.9.4-1.dev0'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'jquery_datatables_plugins', 'test_jquery_datatables.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.jquery_datatables_plugins',
    version=version,
    description="Fanstatic packaging of jQuery Datatables plugins",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Danie. Havlik',
    author_email='dh@gocept.com',
    license='BSD',
    packages=find_packages(),namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
        'js.jquery',
        'js.jquery_datatables'
        ],
    entry_points={
        'fanstatic.libraries': [
            'jquery_datatables_plugins = js.jquery_datatables_plugins:library',
            ],
        },
    )
