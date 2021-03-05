from setuptools import setup

if __name__ == '__main__':

    long_description = open('README').read()

    setup(
        name='clockipy',
        version='1.0',
        description='A simple Python wrapper around Clockify\'s API',
        author='Josias Alvarado',
        author_email='josiasjag@gmail.com',
        url='https://josias-alvarado.me',
        packages=['clockipy.core',],
        long_description=long_description,
        license='MIT',
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Operating System :: OS Independent',
            'Topic :: Software Development',
            'Topic :: Games/Entertainment :: Board Games',
            'Intended Audience :: Developers',
            'Development Status :: 3 - Alpha',
            ],
        )