from setuptools import setup, find_packages

setup(
    name='pyenv_loader',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
    ],
    author='Teemu Vartiainen',
    author_email='teemu@vartiainen.eu',
    description='A package to load environment variables from a .env file.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dewabe/pyenv-loader',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pyenv_loader=pyenv_loader.__init__:main',
        ],
    },
)
