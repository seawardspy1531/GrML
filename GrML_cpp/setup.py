import os, sys

from distutils.core import setup, Extension
from distutils import sysconfig


cpp_args = ['/std:c++17']

grml_module = Extension(
    'GrML', 
    sources=['GrML.cpp'],
    include_dirs=['pybind11/pybind11/include/pybind11/pybind11.h'],
    library_dirs=['C:\\Users\\seawa\\AppData\\Local\\Programs\\Python\\Python311\\libs\\python311.lib', 'C:\\Users\\seawa\\AppData\\Local\\Programs\\Python\\Python311\\libs\\python3.lib'],
    language='c++',
    extra_compile_args=cpp_args,
    )

setup(
    name='GrML',
    version='1.0',
    description='GrML C++ source library',
    ext_modules=[grml_module]
)