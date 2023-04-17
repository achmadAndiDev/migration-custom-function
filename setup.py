from setuptools import setup

from migration_custom_function import __version__

setup(
    name='migration_custom_function',
    version=__version__,

    url='https://github.com/achmadAndiDev/migration-custom-function',
    author='Achmad Andi Setyawan',
    author_email='mas.achmadandi@gmail.com',

    py_modules=['migration_custom_function'],
)

# pip install git+git://github.com/achmadAndiDev/migration-custom-function.git#egg=transform_data