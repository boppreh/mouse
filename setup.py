"""
Usage instructions:

- If you are installing: `python setup.py install`
- If you are developing: `python setup.py sdist --format=zip bdist_wheel --universal bdist_wininst && twine check dist/*`
"""
import mouse

from setuptools import setup
setup(
    name='mouse',
    version=mouse.version,
    author='BoppreH',
    author_email='boppreh@gmail.com',
    packages=['mouse'],
    package_data={'mouse': ['*.md']},
    url='https://github.com/boppreh/mouse',
    license='MIT',
    description='Hook and simulate mouse events on Windows and Linux',
    keywords = 'mouse hook simulate hotkey',

    # Wheel creation breaks with Windows newlines.
    # https://github.com/pypa/setuptools/issues/1126
    long_description=mouse.__doc__.replace('\r\n', '\n'),
    long_description_content_type='text/markdown',

    install_requires=["pyobjc-framework-Quartz; sys_platform=='darwin'"], # OSX-specific dependency
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix :: MacOS',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
