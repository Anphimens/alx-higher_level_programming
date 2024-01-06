# 0x07. Python - Test-driven development

In this project, I started practicing test driven development using `docstring` and `unittest`

## Docstring
A docstring in Python is a string literal used as a commnet at the beginning of a module, function, class, or method definition. Its primary purpose is to provide documentation and information about the code. Docstrings can be assessed using the `__doc__` attribute of an object.

## Unittest
Unittest is a built-in module in Python that provides a testing framework. The `unittest` module is inspired by the testing frameworks found in other languages like Java. It allows you to write test cases, test suites, and perform unit testing on your Python code.

### Here's a brief overview
- Test Case:
    - A test case is the smallest unit of testing in `unittest`. It is created by subclassing `unittest.TestCase`.
    - Test methods within a test case class should start with the "test".


- Test Suite:
    * A test suite is collection of test cases or other test suites. It can be created by combining multiple test cases.
    - A `unittest.TestLoader` class is often used to create test suites.

- Assertions:
    - `unittest` provides various assertion methods (e.g. `assertEqual`, `assertTrue`, `assertFalse`) to check correctness of your code.

* Test Runner:
    - The test runner is responsible for executing the test. Python provides a built-in test runner, and you can tests using the `unittest.main()` function or from the command line using the `python -m unittest` command.


## In this project, you shall see the display of test driven development in use