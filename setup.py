import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="roman-converter",
    version="1.0.0",
    description="Component for converting Roman numbers to arabic and vice versa.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Dainius Arnastauskas",
    author_email="dainius1997@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9.4",
    ],
    packages=["component"],
    include_package_data=True,
)