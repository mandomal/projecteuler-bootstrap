import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="projecteuler-bootstrap",
    version="0.0.1",
    author="Armando Maldonado",
    author_email="mandophysics@gmail.com",
    description=("A bootstrapping tool to set up workspaces for solving a specific projecteuler problem."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pebootstrap = bootstrapper.cli:main",
            "pebs = bootstrapper.cli:main",
        ]
    }
)