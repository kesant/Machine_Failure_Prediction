import os

from setuptools import setup, find_packages

def readme() -> str:
    """Utility function to read the README.md.

    Used for the `long_description`. It's nice, because now
    1) we have a top level README file and
    2) it's easier to type in the README file than to put a raw string in below.

    Args:
        nothing

    Returns:
        String of readed README.md file.
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='machine_failure_prediction',
    version='0.1.0',
    author='mlzoomcamp project',
    author_email='Yout email (or your organization/company/team)',
    description='This project aims to build a predictive model to detect machine failures in advance using sensor data. By analyzing readings such as temperature, air quality, RPM, and electrical current, the model identifies patterns that often precede failures. This predictive maintenance approach helps prevent unexpected downtimes, enhancing operational efficiency and reducing costs associated with machine breakdowns. The project leverages historical sensor data to train machine learning models for accurate and timely failure prediction.',
    python_requires='>=3',
    url='',
    packages=find_packages(),
    long_description=readme(),
)