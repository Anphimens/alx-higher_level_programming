# 0x06. Python - Classes and Objects

# Overview

## Classes
A class is a blueprint or a template for creating objects. It defines a set of attributes and behaviours that its objects will have.

### Attributes
These are variables that store data, defining the characteristics or properties of the objects created from the class.

### Methods
These are functions that define the behaviors or actions that the objects can perform. They are defined within the class and operate on the attributes of the class.

### Object-Oriented Programming (OOP)
Classes are a fundamental concept in Object-Oriented Programming, a programming paradigm that organizes code into objects, representing real-world entities, and the interactions between them.


## Classes
### Instance
An object is an instance of a class. It is created based on the blueprint provided by the class and has its own set of attributes and values

### Instantiation
The process of creating an object from a class is called instantiation. It invloves allocating memory for the object and initializing its attributes.

### Encapsulation
Objects encapsulate data and behaviour within a single unit. The internal detatils of an object are hidden from the outside, and access is controlled through methods.

### Inheritance
A concept where a class can inherit attributes and methods from another class. It promotes code reusability and establishes a relationship between classes.

# Learning Objectives
## General

+ Why Python programming is awesome
+ What is OOP
- “first-class everything”
- What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
- What are and how to use public, protected and private attributes
- What is `self`
* What is a method
- What is the special `__init__` method and how to use it
+ What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
+ What is the Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
- What is the `__dict__` of a class and/or instance of a class and what does it contain
+ How does Python find the attributes of an object or class
+ How to use the `getattr` function


# Requirements
## General
- Allowed editors: `vi`, `vim`, `emacs`
+ All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
* Your code should use the pycodestyle (version `2.8.*`)
+ All your files must be executable
- The length of your files will be tested using `wc`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
+ All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c` `'print(__import__("my_module").MyClass.my_function.__doc__)'`)
