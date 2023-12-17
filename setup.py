from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='pyemailnator',
    version='0.0.1',
    author='nazavod',
    author_email='n4z4v0d@gmail.com',
    description='EmailNator Lib',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/nazavod777/pyemailnator',
    packages=find_packages(),
    install_requires=['requests>=2.31.0',
                      'httpx>=0.24.1',
                      'better_proxy>=0.2.2'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='emailnator smartnator email temp_mail free_mail',
    project_urls={
        'GitHub': 'https://github.com/nazavod777/pyemailnator'
    },
    python_requires='>=3.11'
)
