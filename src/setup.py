from setuptools import find_packages, setup


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name='lgtm',
    version='1.0.0',
    packages=find_packages(exclude=('tests',)),
    install_requires=_requires_from_file('requirements.txt'),
    entry_points={
        'console_scripts': [
            'lgtm=lgtm.core:cli'
        ]
    }
)
