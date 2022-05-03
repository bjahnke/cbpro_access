from setuptools import setup

setup(
    name='cbpro_access',
    version='0.0.0.1',
    packages=['cbpro_access'],
    url='',
    license='',
    author='bjahnke',
    author_email='',
    description='',
    install_requires=[
        'pandas',
        'abstract_broker @ git+https://github.com/bjahnke/abstract_broker.git#egg=abstract_broker',
        'coinbase-pro @ git+https://github.com/teleprint-me/coinbase-pro.git#egg=coinbase-pro',
    ]
)
