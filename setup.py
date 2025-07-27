from setuptools import setup, find_packages
import os

# Read README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="pet-friendly-campsites-israel",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Find pet-friendly camping sites in Israel from Booking.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pet-friendly-campsites-israel",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "campsite-collector=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["data/*.csv", "docs/*.md"],
    },
)
