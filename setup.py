from setuptools import setup, find_packages

setup(
    name='misaki',  # Name of the package
    version='0.2.0',           # Initial version
    packages=find_packages(),  # Automatically finds packages
    install_requires=[         # List your dependencies here
        'num2words',
        'phonemizer',
        'regex',
        'spacy',
        'spacy-curated-transformers',
    ],
    python_requires='>=3.6',  # Minimum Python version required
    author='hexgrad',
    author_email='hello@hexgrad.com',
    description='G2P engine for TTS',
    long_description=open('README.md').read(),  # Content from your README
    long_description_content_type='text/markdown',  # Required for markdown
    url='https://github.com/hexgrad/misaki',  # GitHub repo URL
    license='Apache 2.0',
    classifiers=[  # This helps users discover your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)