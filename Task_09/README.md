# Task 9: Implement and Test the Calculator

## Aim
To implement a complete milk-payment calculator using Python functions, input validation, exception handling, and automated tests.

## 1. Implementation
The calculator uses the following functions:

- `rate_per_litre(fat, snf)`: Calculates the milk rate based on fat and SNF percentages.
- `payout(litres, fat, snf)`: Calculates the payment for the supplied milk quantity.
- `calculate_ten_day_total(payments)`: Calculates the total of the individual payments.

## 2. Formula Used

Fat adjustment steps:

Fat steps = ROUND((Fat percentage − 3.5) / 0.1)

SNF adjustment steps:

SNF steps = ROUND((SNF percentage − 8.5) / 0.1)

Rate per litre:

Rate = ₹30.00 + (Fat steps × ₹0.40) + (SNF steps × ₹0.30)

Payment:

Payment = Milk quantity × Rate per litre

The rate and payment are rounded to two decimal places.

## 3. Testing Strategy

The calculator is tested using:
- Normal entries with fat and SNF above and below the standard values.
- Boundary entries at 3.5% fat and 8.5% SNF, and at the minimum and maximum allowed fat values of 2.0% and 7.0%.
- Invalid entries, including text input, negative milk quantity, and fat outside the allowed range.
- Five valid entries whose individual payments and total are calculated by hand.

### Task 9 – Test Case Table

| S. No. | Test Case | Input | Expected Result | Actual Result |
|---:|---|---|---|---|
| 1 | Standard values | 10 L, Fat 3.5%, SNF 8.5% | Rate: ₹30.00/L; Payment: ₹300.00 | PASS |
| 2 | Fat and SNF above standard | 8.5 L, Fat 4.2%, SNF 8.7% | Rate: ₹33.40/L; Payment: ₹283.90 | PASS |
| 3 | Fat and SNF below standard | 12 L, Fat 3.1%, SNF 8.3% | Rate: ₹27.80/L; Payment: ₹333.60 | PASS |
| 4 | Minimum allowed fat | Fat 2.0%, SNF 8.5% | Rate: ₹24.00/L | PASS |
| 5 | Maximum allowed fat | Fat 7.0%, SNF 8.5% | Rate: ₹44.00/L | PASS |
| 6 | Text quantity | Quantity: `abc` | ValueError | PASS |
| 7 | Negative quantity | Quantity: -5 L | ValueError | PASS |
| 8 | Fat below minimum | Fat 1.9% | ValueError | PASS |
| 9 | Fat above maximum | Fat 7.1% | ValueError | PASS |
| 10 | Five-entry total | 10 L, 8.5 L, 12 L, 5 L, 6 L with the test values above | Total: ₹1,259.50 | PASS |

**Five-entry total calculation:**

₹300.00 + ₹283.90 + ₹333.60 + ₹150.00 + ₹192.00 = **₹1,259.50**

**Conclusion:** All 10 test cases passed. The calculator correctly calculates milk payments, checks valid input ranges, rejects invalid entries, and calculates the total payment.

## 4. Automated Testing with Assertions

A test function uses Python `assert` statements to compare actual results with expected results. This allows multiple test cases to be rerun automatically after changes to the program.

## 5. Alternative Concept and Complexity Analysis

**Manual testing:** Each test input is entered by hand, and the output is compared with the expected result. Repeating all tests after every change requires additional manual effort.

**Automated testing:** A test function executes all test cases and checks their results using assertions. It makes repeated testing faster and more consistent.

For `n` test cases, running the complete test suite takes O(n) time. Manual testing also requires O(n) test executions, but it involves additional human effort. Automated tests are especially useful when the calculator is modified frequently.

## Evidence

The following evidence will be included:
1. **Source code:** `task9.py`, containing the calculator and input validation.
2. **Automated tests:** `test_task9.py`, containing assertions for valid, boundary, and invalid cases.
3. **Test results table:** Expected and actual results for every test case.
4. **Output screenshot:** `Task 9_Output.png`, showing the successful test execution.
5. **Output screenshot:** `Task9_Valid_Input_Output.png`, showing the successful test execution.

## Conclusion
The calculator is implemented and verified using normal, boundary, and invalid test cases. Automated assertions improve repeatability and help detect errors whenever the program is changed.
