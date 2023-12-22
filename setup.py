from setuptools import setup

setup(
    name = 'rubinobot',
    version = '2.1',
    author='Amirali Irvany',
    author_email = 'dev.amirali.irvany@gmail.com',
    description = 'Robinobot is a library for building self-robots in Robino based on API',
    keywords = ['bot', 'Bot', 'rubino', 'rubika', 'rubinobot'],
    long_description = open('README.md', encoding='utf-8').read(),
    python_requires='~=3.6',
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/activate-sh',
    install_requires = ['requests'],
    classifiers = [
    	'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ]
)
