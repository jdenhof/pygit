from setuptools import find_packages, setup

setup(
    name="pygit",
    description="Small collection of git commands in python.",
    version="0.0.1.dev1",
    url="https://github.com/jdenhof/pygit",
    author="Jagger Denhof",
    packages=find_packages(),
    install_requires=[
    ],
    # extras_require={
    #     "test": [
    #         "pytest",
    #         "pytest-cov"
    #     ]
    # }
)
