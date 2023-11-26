from setuptools import setup, find_packages

setup(
    name="reuse_math",
    version="1.0",
    description="SENG 560 reusable arithmatic library.",
    packages=["reuse_math"],
    package_dir={"reuse_math": "src/reuse_math"},
    setup_requires=["setuptools>=56.0"],
    python_requires=">= 3.8"
)