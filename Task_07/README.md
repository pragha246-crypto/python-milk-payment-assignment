# Task 7: Build a Module

## Aim
To create a Python module named `milkrate.py` containing the milk rate card and calculation functions, then import and use it from a separate Python script.

## Concepts Covered

### 1. Creating and Importing a Module
A Python module is a file containing reusable Python code, such as variables, constants, and functions. The `milkrate.py` module contains the rate card, `rate_per_litre()` and `payout()` functions.

### 2. Different Import Methods
- `import milkrate`: Imports the complete module. Functions are accessed using `milkrate.payout()`.
- `from milkrate import payout`: Imports only the specified function, which can be called directly as `payout()`.
- `import milkrate as mr`: Imports the module with the shorter alias `mr`. Functions are accessed using `mr.payout()`.

### 3. The Main Guard
The statement `if __name__ == "__main__":` ensures that the demonstration code runs when `milkrate.py` is executed directly. When another script imports the module, the demonstration code does not run, but its functions and constants remain available. Without the main guard, the demonstration code would also execute during import.

### 4. Standard Modules
Python provides standard modules such as `math` for mathematical operations and `decimal` for accurate decimal arithmetic, which is useful for financial calculations.

### 5. Module Search Path
Python searches for modules using locations listed in `sys.path`, including the script's directory and configured library paths. Keeping `milkrate.py` and the importing script in the same folder makes the module easier to locate.

### 6. Alternative Concept and Complexity Analysis
Copying the calculation functions into multiple scripts duplicates code. Whenever the rate changes, every copy may need updating. Using a shared module allows the rate card and functions to be maintained in one place.

Python loads a module the first time it is imported and stores it in `sys.modules`. Later imports generally reuse the cached module, avoiding repeated loading within the same Python process.

### Evidence
- `milkrate.py` — the module containing the rate card and calculation functions.
- `test_milkrate.py` — a separate script that imports the module and calls `payout()`.
- `Task_07_Output.png` — screenshot showing the successful output.

## Conclusion
The task demonstrates how Python modules improve code reuse, maintainability, and organisation, while the main guard prevents demonstration code from running unnecessarily during imports.
