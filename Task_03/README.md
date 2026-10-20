# Task 3: Choose Variables and Name the Constants

## Aim
To use named constants for milk rates and limits, follow Python naming conventions, and understand dynamic typing and multiple assignment.

## 1. Naming Rules and Conventions
- Variable names should be meaningful and descriptive.
- Python variable names commonly use `snake_case`, such as `rate_per_litre`.
- Constants are conventionally written in `UPPER_CASE`, such as `BASE_RATE` and `FAT_RATE`.
- Names cannot begin with a digit or contain spaces.

## 2. Why Python Has No True Constants
Python does not enforce constants as immutable variables. Uppercase names are a convention that tells programmers a value should not be changed during normal program execution.

## 3. Dynamic Typing
Python allows a variable to refer to values of different types during execution. For example:

`value = 10` — the value is an integer (`int`).

`value = "Milk"` — the same variable now refers to a string (`str`).

## 4. Multiple Assignment and Swapping
Python supports assigning multiple variables in one statement:

`a, b = 5, 10`

Variables can be swapped without a temporary variable:

`a, b = b, a`

After swapping, `a` becomes 10 and `b` becomes 5.

## 5. Rate-Revision Complexity
Using named constants such as `BASE_RATE`, `FAT_RATE`, and `SNF_RATE` allows a rate revision to be made in one place for each affected constant. If values are hard-coded as magic numbers in multiple expressions, every occurrence may need to be updated, increasing the chance of mistakes.

A dictionary such as `RATE_CARD` can also store related rates in one place, but the program must consistently retrieve values from that dictionary.

## 6. Time and Memory Analysis
Changing constants or dictionary values does not significantly change the program's running time or memory usage. The main benefit is easier maintenance, fewer repeated edits, and reduced risk of errors.

## Evidence
- Python program: `task3.py`
- Output screenshot: `Task_03_Output.png`
