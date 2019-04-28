"""
A python-based software delivery pipeline generator.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pypefitter',
    version='0.0.1',
    description='A python-based software delivery pipeline generator.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/christopheralanjones/pypefitter',
    author='Christopher A. Jones',
    author_email='christopher.jones@depaul.edu',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='build deploy development',

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip install' will check this
    # and refuse to install the project if the version does not match. If you
    # do not support Python 2, you can simplify this to '>=3.5' or similar, see
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires='>=3.7',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['antlr4-python3-runtime>=4.7', 'argparse>=1.4.0', 'jinja2>=2.10'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={  # Optional
        'dev':  ['sphinx>=2.0', 'blurb>=1.0', 'python-docs-theme>=2018.7'],
        'test': ['coverage>=4.5',  'flake8>=3.7', 'pytest>=4.4', 'pytest-cov>=2.6'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    #
    # If using Python 2.6 or earlier, then these have to be included in
    # MANIFEST.in as well.
    # package_data={
    #     'sample': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        'console_scripts': [
            'pypefitter=pypefitter:main',
        ],
        'pypefitter.providers': [
            'jenkins=pypefitter.providers.jenkins:JenkinsProvider',
            'aws=pypefitter.providers.aws:AwsProvider'
        ],
        'pypefitter.providers.actions': [
            'generate=pypefitter.api.action:GenerateAction',
            'init=pypefitter.api.action:InitAction',
            'validate=pypefitter.api.action:ValidateAction'
        ],
        'pypefitter.providers.jenkins.emitters': [
            'jenkinsfile=pypefitter.emitters.jenkinsfile:JenkinsfileEmitter'
        ],
        'pypefitter.providers.aws.emitters': [
            'terraform=pypefitter.emitters.terraform:TerraformEmitter',
            'cloudformation=pypefitter.emitters.cloudformation:CloudFormationEmitter',
        ],
    },

    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    project_urls={
        'Bug Reports': 'https://github.com/christopheralanjones/pypefitter/issues',
        # 'Funding': 'https://donate.pypi.org',
        # 'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/christopheralanjones/pypefitter',
        'Wiki': 'https://github.com/christopheralanjones/pypefitter/wiki',
    },
)