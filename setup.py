from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quote-gen",
    version="0.1.0",
    author="Sai Srinivas Reddy Musirika",
    author_email="musirikasrinivas@gmail.com",
    description="A Python library for generating quotes using AI",
    url="https://github.com/musirikasrinivas/quote_generator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "anthropic>=0.3.0",
    ],
)