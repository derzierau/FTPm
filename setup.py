from setuptools import setup

setup(
    name="freilanz",
    version="0.1.0",
    description="CLI Freelancing Suite",
    author="Ole Zierau",
    author_email="kontakt@olezierau.de",
    packages=["freilanz", "freilanz.commands"],
    scripts=["bin/lanz"],
    install_requires=[
        "Click>=7.0,<8.0",
        "pandas>=1.0.1,<2",
        "PyYAML>=5.0,<6.0",
        "appdirs==1.4.3",
        "colorama"
    ],
)
