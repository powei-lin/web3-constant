import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="web3-constant",
    version="0.0.6",
    author="Powei Lin",
    author_email="poweilin1994@gmail.com",
    description="Useful web3 constant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/powei-lin/web3-constant",
    project_urls={
        "Bug Tracker": "https://github.com/powei-lin/web3-constant/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
)
