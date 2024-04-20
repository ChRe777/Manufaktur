from setuptools import setup, find_packages

setup(
    name="Manufaktur",
    version="0.0.2",  # MAJOR.MINOR.PATCH
    packages=find_packages(),
    license="MIT",
    description="A Manufaktur package",
    long_description=open("README.md").read(),
    install_requires=["goless == 0.7.2", "gevent == 24.2.1"],
)
