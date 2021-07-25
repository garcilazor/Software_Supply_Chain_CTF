from setuptools import setup
setup(name='emailpackage', 
    version='0.1',
    description='Email Package Python Package', 
    author='@huy', 
    author_email='', 
    license='MIT', 
    packages=['emailpackage'],
    install_requires=
    [
        'PyMySQL'
    ],      
    zip_safe=False)