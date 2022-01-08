import tqmath
from setuptools import setup, find_packages

install_requires = [
    "setuptools",
    "numpy"
]


def long_description():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name='tqmath',
    version=tqmath.__version__,
    description=tqmath.__doc__.strip(),
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/farooq-teqniqly/python-wheels',
    author=tqmath.__author__,
    author_email='farooq@teqniqly.com',
    license=tqmath.__license__,
    packages=find_packages(include=['tqmath', 'tqmath.*']),
    entry_points={
        'console_scripts': [
            'tq-math = tqmath.__main__:main'
        ],
    },
    python_requires='>=3.6',
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Utilities'
    ],
    project_urls={
        'GitHub': 'https://github.com/farooq-teqniqly/python-wheels'
    },
)
