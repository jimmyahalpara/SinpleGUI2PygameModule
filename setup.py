from setuptools import setup






# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    ]

# calling the setup function 
setup(name='Pytable',
      version='1.0.0',
      description='module for making tables in python',
      long_description='module for making tables in python',
      url='https://github.com/jimmyahalpara/Pytable',
      author='Jimmy Kumar Ahalpara',
      author_email='jimmyahalpara123@gmail.com',
      license='MIT',
      packages=['Pytable'],
      classifiers=CLASSIFIERS,
      keywords='tables'
      )
