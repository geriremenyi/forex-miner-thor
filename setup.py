import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="com.geriremenyi.forex-miner-thor",
    version="0.0.1",
    author="Gergely Reményi",
    author_email="geri@geriremenyi.com",
    description="Trading engine of the forex-miner.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/geriremenyi/forex-miner-thor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
