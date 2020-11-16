import setuptools

setuptools.setup(
    name="forex_miner_thor",
    version="0.0.1",
    author="Gergely Remenyi",
    author_email="geri@geriremenyi.com",
    description="Trading engine of the forex-miner.com",
    url="https://github.com/geriremenyi/forex-miner-thor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
