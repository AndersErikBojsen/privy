from setuptools import find_packages, setup

setup(
    name='privy',
    version='6.0.0',
    description='An easy, fast lib to correctly password-protect your data',
    long_description=open('README.rst', 'r').read(),
    author='Ofek Lev',
    author_email='ofekmeister@gmail.com',
    url='https://github.com/ofek/privy',
    license='MIT/Apache-2.0',

    keywords=(
        'passwords',
        'secrets',
        'encryption',
        'keys',
        'aes',
        'hmac',
    ),

    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),

    install_requires=['cryptography', 'argon2_cffi'],
    tests_require=['pytest'],

    packages=find_packages(),
)
