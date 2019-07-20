# requests-python


--------
POM API automation test requests
--------


------
Setup 
------

The setup has 4 parts:

1. Prerequisites 
2. How to run test cases
3. Code


__1. Prerequisites__

a) Install Python 3.x

b) Add Python 3.x to your PATH environment variable

c) If you do not have it, get pip (NOTE: Most recent Python distributions come with pip)

d) Input command in terminal : pip install pipenv 
####Note: Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.
   > [pipenv homepage](https://github.com/pypa/pipenv)

e) git clone this project, and go to root, run command pipenv install, all the dependencies will install automatically. 


__2. How to run test cases__

a) Environment url setting are in config.ini
path as /Config/config.ini

b) entrance.py is the main for unittest, you can run different test cases via command line.


__3. Code__

a) /Common/base_test.py it's the base class, and include public method.

c) /TestCase folder include test cases.

d) /logs folder include log function and logs saved.

e) /report folder include test report saved here.

f) Pipfile and Pipfile.lock are pipenv file include dependencies information.
