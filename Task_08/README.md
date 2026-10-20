# Task 8: Plan the Algorithm Before Coding

## Aim
To plan an algorithm for calculating one farmer's milk payment and the total payment for ten days using pseudocode, a flowchart, and a hand trace before writing the Python program.

## 1. Steps of Algorithmic Problem Solving

1. **Understand:** Identify the inputs required: milk quantity, fat percentage, and SNF percentage.
2. **Plan:** Define the rate calculation, payment calculation, input validation, and ten-day total.
3. **Write:** Convert the planned algorithm into Python code using clear variables and functions.
4. **Test:** Test normal inputs, invalid entries, and the calculated results against expected values.

## 2. Pseudocode

**Algorithm: Calculate One Payment and Ten-Day Total**

**BEGIN**

1. Set `BASE_RATE = 30.00`, `FAT_STEP_VALUE = 0.40`, and `SNF_STEP_VALUE = 0.30`.
2. Set `TOTAL_PAYMENT = 0`.
3. Repeat for each of the ten daily entries:
   - Read `LITRES`, `FAT`, and `SNF`.
   - If any input is invalid or negative, display an error and request a valid entry.
   - Calculate `FAT_STEPS = ROUND((FAT - 3.5) / 0.1)`.
   - Calculate `SNF_STEPS = ROUND((SNF - 8.5) / 0.1)`.
   - Calculate `RATE = ROUND(BASE_RATE + FAT_STEPS × FAT_STEP_VALUE + SNF_STEPS × SNF_STEP_VALUE, 2)`.
   - Calculate `PAYMENT = ROUND(LITRES × RATE, 2)`.
   - Display `RATE` and `PAYMENT`.
   - Update `TOTAL_PAYMENT = TOTAL_PAYMENT + PAYMENT`.
4. Display `TOTAL_PAYMENT`.

**END**

## 3. Flowchart for Validating One Entry

BEGIN → Read quantity, fat, and SNF → Are all inputs numeric and non-negative?

- **NO:** Display an error message → Request the entry again.
- **YES:** Calculate the rate → Calculate payment → Display results → END.

## 4. Hand Trace for Three Entries

Use the rate formula and calculate each payment separately.

| Entry | Litres | Fat (%) | SNF (%) | Rate (₹/L) | Payment (₹) |
|---|---:|---:|---:|---:|---:|
| 1 | 10.0 | 3.5 | 8.5 | 30.00 | 300.00 |
| 2 | 8.5 | 4.2 | 8.7 | 33.40 | 283.90 |
| 3 | 12.0 | 3.1 | 8.3 | 27.80 | 333.60 |
| **Total** | **30.5** | — | — | — | **917.50** |

The running total is ₹300.00 after Entry 1, ₹583.90 after Entry 2, and ₹917.50 after Entry 3.

## 5. Alternative Concepts and Complexity Analysis

**Method A — Store all entries:** Store the daily entries or payments in a list and add them at the end. The time complexity is O(n), and the space complexity is O(n).

**Method B — Running total:** Add each payment to `TOTAL_PAYMENT` immediately after calculating it. The time complexity is O(n), and the extra space complexity is O(1) when only the running total and current entry are stored.

Storing entries is useful when the program must display a history, revise a previous entry, sort records, or calculate additional statistics later.

## 6. Evidence

The following evidence is provided to demonstrate the algorithmic planning and implementation:

1. **Pseudocode:** The step-by-step algorithm for calculating one farmer's milk payment and the ten-day total.
2. **Flowchart:** `Task_08_Flowchart.png`, showing input validation, error handling, rate calculation, and payment calculation.
3. **Hand Trace:** A table showing three sample entries, individual payments, and the running total of ₹917.50.
4. **Python Program:** `task8.py`, implementing the planned algorithm with input validation and a running total.
5. **Program Output:** `Task_8_Output.png`, showing the program's execution and calculated payment results.

These items demonstrate that the algorithm was planned, traced, implemented, and tested before completion.

## Conclusion
Pseudocode, a flowchart, and a hand trace help verify the calculation logic before implementation. Both approaches require O(n) time, while a running total uses less additional memory.
