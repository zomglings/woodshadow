from setuptools import find_packages, setup

long_description = ""
with open("README.md") as ifp:
    long_description = ifp.read()

with open("woodshadow/version.txt") as ifp:
    VERSION = ifp.read().strip()

setup(
    name="woodshadow",
    version=VERSION,
    packages=find_packages(),
    install_requires=["eth-brownie", "moonworm", "tqdm"],
    extras_require={
        "dev": ["black", "mypy"],
        "distribute": ["setuptools", "twine", "wheel"],
    },
    description="woodshadow - Dark Forest bots and analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="zomglings",
    author_email="nkashy1@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
    url="https://github.com/zomglings/woodshadow",
    entry_points={
        "console_scripts": [
            "ws=woodshadow.cli:main",
        ]
    },
    package_data={
        "woodshadow": [
            "version.txt",
            "abis/*.json",
            "fixtures/*.json",
            "fixtures/*.jsonl",
        ]
    },
    include_package_data=True,
)
