from setuptools import setup

setup(
   name='Dawg',
   version='1.0',
   description='Fake news Detector',
   author='Abolo Samuel',
   author_email='ikabolo59@gmail.com',
   packages=['dawg'],  #same as name
   install_requires=['flask', 'numpy', 'pandas', 'joblib', 'sklearn', 'flask-cors'], #external packages as dependencies
)
