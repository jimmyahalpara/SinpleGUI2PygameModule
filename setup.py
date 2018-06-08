import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pytable",
    version="1.0.0",
    author="jimmy kumar ahalpara",
    author_email="jimmyahalpara123@gmail.com",
    description="can be used to create tables in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jimmyahalpara/Pytable/tree/Pytable",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
