# PyMake

A more lightweight alternative to CMake

## Problem

I wanted a more simple version of CMake for making personal projects. All the tools that are for C++ feel outdated. I wanted a more modern tool for compiling C/C++.

## How to get

- download the main.py file

- download the PyMake.json file

- run main.py

## settings in PyMake.json

- compiler : which c/c++ compiler to use

- out: the name of file. if left blank, compiler with default to a.out if on linix

- warnings : turns on flags to catch any warnings

- libs : these are all libarys you want included. You do not need to include -l for them

- version: which version to use for the compiler

- wipe : deletes the executable before compiling code

- file_types : the files that you want to compile (.cpp, .c, .h, .hpp)