# Python version

import sys

py_version = sys.version

print("Python version is: ", py_version)
print("Python version is: ", sys.version_info)


# using platform module

import platform


version = platform.python_version()

print("version is: ", version)
version = platform.python_version_tuple()

print("Version as tuple is: ", version)

version = type(platform.python_version_tuple())
print("Type is: ", version)




