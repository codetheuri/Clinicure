from setuptools import setup

version = re.search("__version__ = '([^']+)'", open('$PROJECT_NAME/__init__.py').read()).group(1)

setup(
    name="$PROJECT_NAME",
    version=version,
    description="$DESCRIPTION",
    url="<url>",
    author="$AUTHOR",
    author_email="<email>",
    keywords="<keywords>",
    license="<license>",
    packages=["resources"],
    include_package_data=True,
    # classifiers can be found here: https://pypi.python.org/pypi?%3Aaction=list_classifiers 
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'License :: OSI Approved :: MIT License',
        
        # Python 2 Only?
        'Programming Language :: Python :: 2'
        'Programming Language :: Python :: 2.3'
        'Programming Language :: Python :: 2.4'
        'Programming Language :: Python :: 2.5'
        'Programming Language :: Python :: 2.6'
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: 2 :: Only'

        # Python 3 Only?
        'Programming Language :: Python :: 3'
        'Programming Language :: Python :: 3.0'
        'Programming Language :: Python :: 3.1'
        'Programming Language :: Python :: 3.2'
        'Programming Language :: Python :: 3.3'
        'Programming Language :: Python :: 3.4'
        'Programming Language :: Python :: 3 :: Only'

        # Python 2 and 3?
        'Programming Language :: Python :: 2'
        'Programming Language :: Python :: 2.3'
        'Programming Language :: Python :: 2.4'
        'Programming Language :: Python :: 2.5'
        'Programming Language :: Python :: 2.6'
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: 3'
        'Programming Language :: Python :: 3.0'
        'Programming Language :: Python :: 3.1'
        'Programming Language :: Python :: 3.2'
        'Programming Language :: Python :: 3.3'
        'Programming Language :: Python :: 3.4'
    ],
)


    ],
)

