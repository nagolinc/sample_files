from setuptools import setup, find_packages

setup(
    name='sample_files',           # Name you will `pip install`
    version='0.1',
    description='Sample lines from text or JSON files',
    author='Your Name',
    packages=find_packages(),       # This automatically finds your `sample_files/`
    python_requires='>=3.6',         # Adjust if needed
)
