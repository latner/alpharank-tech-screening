from setuptools import setup, find_packages

setup(
    name="alpharank-screening",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas>=2.0.0",
        "requests>=2.28.2",
        "sqlalchemy>=1.4.46",
        "python-dotenv>=1.0.0",
        "beautifulsoup4>=4.12.0",
        "lxml>=4.9.2",
    ],
    extras_require={
        "dev": [
            "pytest>=7.3.1",
            "pytest-cov>=4.1.0",
            "black>=23.3.0",
            "flake8>=6.0.0",
            "mypy>=1.3.0",
            "jupyter>=1.0.0",
            "ipywidgets>=8.0.6",
        ]
    },
    python_requires=">=3.9",
    author="Bryan Latner",
    description="Technical screening project for Alpharank",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
