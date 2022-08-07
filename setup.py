# Setup.py

# Imports
from setuptools import setup, find_packages

# Reading Files
with open('README.md') as readme_file:
    README = readme_file.read()

# Setup Arguements
setup_args = dict (
    name='PyMathSolver',
    version='1.0.2',
    description='Python module to solve math problems and work on calculations.',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    author='Aniketh Chavare',
    author_email='anikethchavare@outlook.com',
    keywords=['Math', 'Calculations'],
    url='https://github.com/Anikethc/PyMathSolver',
    download_url='https://pypi.org/project/pymathsolver'
)

# Necessary Installs of Packages
install_requires = [
    'termcolor'
]

# Run the Setup File
if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)