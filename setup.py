from setuptools import setup, find_packages

setup(
    name="python-modifiers",
    version="0.0.1",
    description="Access modifiers like private, protected, and public for Python",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='TechAngle',
    url='https://github.com/TechAngle/python-modifiers',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'LICENSE :: MIT License'
    ]
)