from setuptools import setup

setup(
    name='knackpy',
    version='0.0.2',
    description='Python API wrapper for interacting with Knack applications.',
    url='http://github.com/cityofaustin/knack-py',
    author='John Clary',
    author_email='john.clary@austintexas.gov',
    license='Public Domain',
    packages=['knackpy'],
    install_requires=[
      'arrow',
      'requests'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
