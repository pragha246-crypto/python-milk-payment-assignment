# Task 5: Read Input and Convert Types

## Aim
To read the clerk's entries, convert input strings into numeric values, handle invalid inputs, and display neatly formatted results.

## Topics Covered
- Using `input()` to read text
- Converting values with `int()` and `float()`
- Handling invalid entries such as `8,5` and `eight`
- Validating input using string methods
- Handling conversion errors using `try/except ValueError`
- Formatting output using f-strings, width, and precision
- Comparing validation approaches and their time complexity

## 1. Why `input()` Returns a String

Python's `input()` function returns the entered value as a string. Numeric calculations require conversion using `float()` or `int()`.

## 2. Handling Invalid Input

- `8.5` is accepted as a valid decimal number.
- `8,5` is rejected because Python does not use a comma as a decimal separator.
- `eight` is rejected because it cannot be converted to a number.

## 3. String Validation vs. `try/except`

String methods can check the format of an input before conversion, but they may not handle every valid numeric format. Using `try/except ValueError` catches conversion failures directly and makes the program more robust.

## 4. Formatted Output

F-strings allow numbers to be displayed with two decimal places using `.2f`. Width and alignment specifiers help organize the output into readable columns.

## 5. Time and Space Complexity

For a fixed number of input fields, conversion and formatting take O(1) time and O(1) auxiliary space. The demonstration loop has three fixed examples, so its total complexity is also O(1).

## Evidence
- Python program: `task5.py`
- Valid-input screenshot: `Task_05_Output.png`
- Invalid-input screenshot: `Task_05_Invalid_Input.png`
