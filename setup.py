from setuptools import setup, find_packages

setup(
    name = 'rubinobot',
    version = '1.3',
    author='Amirali Irvany',
    author_email = 'dev.amirali.irvany@gmail.com',
    description = 'none',
    keywords = ['bot', 'Bot', 'rubino', 'rubino', 'rubinobot'],
    long_description = open('README.md', encoding='utf-8').read(),
    python_requires='~=3.6',
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/activate-sh',
    packages = find_packages(),
    install_requires = [],
    classifiers = [
    	'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ]
)
