from setuptools import setup

setup(
    name='tbuilder',
    python_requires=">=3.0",
    version='0.0.1',
    description='A tool to build and test python packages.',
    author='Sergey Zakharov',
    author_email='sergzach@gmail.com',
    install_requires=[
        'readingproc>=0.0.1'
    ],
    scripts=['tbuilder.py'],
    py_modules=['downloaders', 'testchecker']
)