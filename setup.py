"""
Setup script for Lexi AI
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lexi-ai",
    version="0.1.0",
    author="Lexi AI Team",
    description="Hyper-personalized AI assistant with ethical guardrails",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/camilesoria/LexiAI",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "python-dateutil>=2.8.2",
        "pyyaml>=6.0",
    ],
    entry_points={
        'console_scripts': [
            'lexi=cli:main',
        ],
    },
)
