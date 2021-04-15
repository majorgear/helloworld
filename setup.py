from setuptools import setup
from helloworld import __version__ as version
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')


setup(name='helloworld',
      version='1.0',
      py_modules=['helloworld'],
      url='',
      author='Major Gear',
      author_email='majorgear@majorgear.tech', 
      description='Prints Hello World'
      long_description=long_description,
      
      )

