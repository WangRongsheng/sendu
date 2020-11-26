import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sendu",
    version="0.0.1",
    author="WangRongsheng",
    author_email="wrswyz@88.com",
    description="Serverjiang for python.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/WangRongsheng/sendu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
