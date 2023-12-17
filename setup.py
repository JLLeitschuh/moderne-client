#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="moderne-client",
    version="0.0.1",
    author="Jonathan Leitschuh",
    author_email="Jonathan.Leitschuh@gmail.com",
    description="A client for the Moderne service.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JLLeitschuh/moderne-client",
    package_dir={'': 'src'},
    packages=find_packages(where="src"),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.9',
    install_requires=[
        "gql[all]>=3.4.0",
        "requests>=2.28.2",
        "PyYAML>=6.0",
        "python-liquid>=1.8.1"
    ],
    extras_require={
        "cli": [
            "rich>=11.0.0",
            "rich-argparse>=1.0.0",
            "isodate>=0.6.1",
            "python-dotenv>=1.0.0",
            "python-gnupg>=0.5.1"
        ],
        "github-scripts": [
            "croniter>=1.3.8",
            "pytz>=2022",
        ],
        "test": [
            "pytest>=6",
            "pytest-cov",
            "Markdown>=3.4.1",
            "aiohttp>=3.8.4",
            "aiounittest>=1.4.2"
        ]
    },
    entry_points={
        "console_scripts": [
            "moderne-client=moderne_client.__main__:cli",
        ],
    },
)
