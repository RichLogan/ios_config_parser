from setuptools import setup
import re

version = ''

with open('ios_config_parser/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

print 'VER:', version

with open('README.md') as f:
    readme = f.read()

packages = ['ios_config_parser']
requires = ['fabric']

setup(
    name='ios_config_parser',
    version=version,
    long_description=readme,
    packages=packages,
    install_requires=requires,
    url='http://github.com/RichLogan/ios_config_parser',
    license='',
    author='rilogan',
    author_email='rilogan@cisco.com',
    description='Python IOS Config Parser'
)
