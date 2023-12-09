# 0x03. Python - Data Structures: Lists, Tuples

## Introduction
Python is a high-level, interpreted, and general-purpose programming languageknown for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

## Key Features
- 1. **Readability**: Python's syntax emphasizes readability, making it easy developers to write clean and maintainable code.
- 2. **Dynamic Typing**: Python is dynamically typed, allowing variables to change types during runtime. This provides flexibility but requires careful attention.
- 3. **Interpreted language**: Python code is executed line by line by the Python interpreter, which makes it easy to test and debug.
- 4. **Extensive Standard library**: Python comes with a vast Standard library that includes modules and packages for various tasks, minimizing the need for external libraries.

## Data Structures
Python provides built-in data structures, including:

- Lists: Ordered, mutable collection of elements.
```
my_list = [1, 2, 3, 4]
```

+ Tuples: Ordered, immutable collections of elements.
```
my_tuple = (1, 2, 3, 4)
```


**This is a project by ALX school.**

## Requirements
### Python Scripts
+ Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
+ The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version `2.8.*`)
+ All your files must be executable
+ The length of your files will be tested using `wc`


## C 
+ Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line


# Tasks 
 0. Write a function that prints all integers of a list. 
[Prints a list of integers](https://github.com/Anphimens/alx-higher_level_programming/blob/master/0x03-python-data_structures/0-print_list_integer.py)

 1. Write a function that retrieves an element from a list in C
[Secure access to an element in a list](./0x03-python-data_structures/1-element_at.py)
	- Prototype: `def element_at(my_list, idx):`
	* If `idx` is negative, the function should return None
	* If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
	+ You are not allowed to import any module
	+ You are not allowed to use `try/except`

 2. Write a function that replaces an element of a list at a specific position (like in C).
[Replace element](./0x03-python-data_structures/2-replace_in_list.py)
	+ Prototype: `def replace_in_list(my_list, idx, element):`
	- If `idx` is negative, the function should not modify anything, and returns the original list
	* If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
	+ You are not allowed to import any module
	- You are not allowed to use `try/except`

 3. Write a function that prints all integers of a list, in reverse order.
[Prints a list of integers...in reverse!](./0x03-python-data_structures/3-print_reversed_list_integer.py)
	+ Prototype: `def print_reversed_list_integer(my_list=[]):`
	- Format: one integer per line. See example
	* You are not allowed to import any module
	+ You can assume that the list only contains integers
	- You are not allowed to cast integers into strings
	* You have to use `str.format()` to print integers


 4. Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
[Replace in a copy](./0x03-python-data_structures/4-new_in_list.py)
	- Prototype: `def new_in_list(my_list, idx, element):`
	* If idx is negative, the function should return a copy of the original `list`
	+ If idx is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`
	- You are not allowed to import any module
	- You are not allowed to use `try/except`


 5. Write a function that removes all characters `c` and `C` from a string
[Can you C me now?](./0x03-python-data_structures/5-no_c.py)


 6. Write a function that prints a matrix of integers.
[Lists of lists = Matrix](./0x03-python-data_structures/6-print_matrix_integer.py)


 7. Write a function that adds 2 tuples.
[Tuples addition](./0x03-python-data_structures/7-add_tuple.py)
	+ Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
	* Returns a tuple with 2 integers:
    		- The first element should be the addition of the first element of each argument
    		- The second element should be the addition of the second element of each argument
	* You are not allowed to import any module
	+ You can assume that the two tuples will only contain integers
	- If a tuple is smaller than 2, use the value `0` for each missing integer
	+ If a tuple is bigger than 2, use only the first 2 integers


 8. Write a function that returns a tuple with the length of a string and its first character.
[More return!](./0x03-python-data_structures/8-multiple_returns.py)
	- Prototype: `def multiple_returns(sentence):`
	+ If the sentence is empty, the first character should be equal to None
	* You are not allowed to import any module


 9. Write a function that finds the biggest integer of a list.
[Find the max](./0x03-python-data_structures/9-max_integer.py)

 10. Write a function that finds all multiples of 2 in a list.
[Only by 2](./0x03-python-data_structures/10-divisible_by_2.py)

 11. Write a function that deletes the item at a specific position in a list.
[Delete at](./0x03-python-data_structures/11-delete_at.py)

 12. Complete the source code in order to switch value of `a` and `b`
[Switch](./0x03-python-data_structures/12-switch.py)
	+ You can find the source code [here](https://github.com/alx-tools/0x03.py/blob/master/12-switch_py)
	* Your code should be inserted where the comment is (line 4)
	- Your program should be exactly 5 lines long

 13. Write a function in C that checks if a singly linked list is a palindrome
[Linked list palindrome](./0x03-python-data_structures/13-is_palindrome.c)
[Header file](https://github.com/Anphimens/alx-higher_level_programming/blob/master/0x03-python-data_structures/lists.h)

