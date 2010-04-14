from setuptools import setup, find_packages
    
version='0.1'
setup(
    name='mongoobject',
    version=version,
    description='Mongo Object',
    author='Matt George',
    author_email='mgeorge@gmail.com',
    maintainer='Matt George',
    license='MIT',
    url='http://github.com/binarydud/mongoobject',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    install_requires=[
        'pymongo==1.5.1',
    ],
    classifiers = [
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python'],
)