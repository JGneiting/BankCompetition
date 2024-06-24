from setuptools import setup, find_packages

setup(
    name="bankcompetition",
    version="0.1.0",
    description="A description of your bank competition project",
    author="Joshua Gneiting",
    author_email="gneitingj9@gmail.com",
    url="https://github.com/JGneiting/BankCompetition.git",
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    entry_points={
        "console_scripts": [
            # Define console scripts here if needed
        ],
    },
)