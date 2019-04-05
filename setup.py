from setuptools import setup, find_packages

setup(
    name="sentry-distutils",
    version="0.0.1",
    description="Sentry's distutils.",
    license="Apache 2.0",
    url="https://github.com/getsentry/sentry-distutils",
    author='Sentry',
    author_email='hello@sentry.io',
    package_dir={'': 'src'},
    packages=find_packages('src'),
)
