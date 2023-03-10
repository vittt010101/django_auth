from setuptools import setup

setup(
   name='foo',
   version='2.0',
   description='Something different',
   author='Jinku Hu',
   author_email='foomail@foo.com',
   packages=['foo'],  # would be the same as name
   install_requires=['wheel', 'bar', 'greek'], #external packages acting as dependencies
)