"""
Usage instructions:

- If you are installing: `python setup.py install`
- If you are developing: `python setup.py sdist bdist --format=zip bdist_wheel --universal`
"""
import sys
import mouse
try:
    import pypandoc
    long_description = pypandoc.convert_text(mouse.__doc__ or '', format='md', to='rst')
except ImportError:
    long_description = mouse.__doc__ or ''

import re
last_version_match = re.search('(\d+(?:\.\d+)+)', open('CHANGES.md').read())
if last_version_match:
    last_version = last_version_match.group(1)
else:
    last_version = '0.0.1'

# Wheel creation breaks with Windows newlines.
# https://github.com/pypa/setuptools/issues/1126
long_description = long_description.replace('\r\n', '\n')

from setuptools import setup
setup(
    name='mouse',
    version=last_version,
    author='BoppreH',
    author_email='boppreh@gmail.com',
    packages=['mouse'],
    url='https://github.com/boppreh/mouse',
    license='MIT',
    description='Hook and simulate global mouse events in pure Python',
    keywords = 'mouse listen hook simulate automate',
    long_description=long_description,
    install_requires=[] + (["pyobjc"] if sys.platform == "darwin" else []), # OSX-specific dependency
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
