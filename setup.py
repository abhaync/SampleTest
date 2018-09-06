import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SampleTest",
    version="0.0.1",
    author="Abhay",
    description="Sample Test Package",
    url="https://github.com/abhaync/SampleTest",
    packages=setuptools.find_packages()
)