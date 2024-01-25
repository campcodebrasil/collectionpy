from setuptools import setup
import os

# Carregar o conteúdo do arquivo README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pylib',
    version='0.0.0',
    description='PyLib is more than just a library; it is a comprehensive tool that provides efficient solutions for various areas, ranging from date manipulation and text formatting to the creation of impressive graphics.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['pylib', 'pylib.chart', 'pylib.date', 'pylib.math', 'pylib.text'],
    install_requires=[],
)