import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycof",
    version="1.1.38",
    author="Florian Felice",
    author_email="florian.felice@outlook.com",
    description="A package for commonly used functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.florianfelice.com/pycof",
    packages=setuptools.find_packages(),
    install_requires=[
          "pandas>=0.24.1",
          "numpy>=1.16.3",
          "psycopg2-binary>=2.7.4",
          "pymysql>=0.9.3",
          "tqdm>=4.35.0",
          "boto3>=1.9.219",
          "xlrd>=1.2.0",
          "matplotlib>=3.1.1",
          "pyarrow>=0.16.0"
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)