from distutils.core import setup

setup(
    name='pyHub',
    version='0.1.0',
    author='pal25',
    author_email='pal25@case[dot]edu',
    packages=['pyHub', 'test'],
    scripts=[],
    url='http://github.com/pal25/pyHub',
    license='',
    description='Python implementation of the ADC protocol using Twisted.',
    long_description=open('README.md').read(),
    install_requires=[
    ],
)
