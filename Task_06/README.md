# Task 6: Organise the Logic into Functions

## Aim
To divide milk-payment calculations into reusable Python functions with parameters, return values, and docstrings.

## Topics Covered
- Defining functions for rate calculation and payout
- Passing parameters and returning values
- Difference between `return` and `print()`
- Local and global variable scope
- Using constants safely inside functions
- Writing docstrings for every function
- Comparing functions with a single long script and lambda expressions
- Time and space complexity

## 1. Functions, Parameters, and Return Values

- `rate_per_litre(fat, snf)` accepts fat and SNF percentages and returns the calculated rate.
- `payout(quantity, rate)` accepts the milk quantity and rate and returns the payment.
- `ten_day_total(daily_quantities, rate)` accepts daily quantities and the rate and returns the total payment.
- `main()` coordinates the calculations and displays the results.

## 2. Returning a Value vs. Printing It

`return` sends a result back to the calling code so it can be stored or reused. `print()` only displays information on the screen. Returning values makes functions easier to reuse and test.

## 3. Local and Global Scope

Function parameters and variables defined inside a function are local to that function. The rate constants are defined at module level and can be read inside the calculation function. They should not be reassigned inside the function.

## 4. Docstrings

Each function has a docstring describing its purpose. Docstrings help other programmers understand and maintain the code.

## 5. Functions vs. a Long Script or Lambda Expressions

Functions reduce repeated code and make individual calculations easier to test. A single long script can duplicate logic, while lambda expressions are best suited to simple expressions and are less suitable for multi-step calculations.

## 6. Time and Space Complexity

The rate and payout functions take O(1) time and O(1) auxiliary space. The ten-day total takes O(n) time for n daily quantities. Function-call overhead is generally small and does not change these asymptotic complexities.

## Evidence
- Python program: `task6.py`
- Output screenshot: `Task_06_Output.png`
