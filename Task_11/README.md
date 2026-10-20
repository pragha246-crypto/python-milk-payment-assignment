# Task 11 – Recommend and Defend the Final Design

## Aim
To recommend a reliable milk-payment calculator for the co-operative based on the experiments conducted in Tasks 9 and 10.

## 1. Recommended Data Types and Rounding Rule

I recommend using Python's `Decimal` type for financial calculations because it supports decimal arithmetic and avoids many binary floating-point representation issues.

The program should convert input values to `Decimal` from strings rather than converting from `float`.

Each farmer's payment should be rounded to two decimal places using a documented rounding rule, such as `ROUND_HALF_UP`, if that rule is approved by the co-operative. The rounded individual payments should then be added to calculate the final amount payable.

In Task 10, float and Decimal produced identical totals for 300, 6,000, and 150,000 test payments, with an observed difference of ₹0.00. However, this result applies to the tested values and does not prove that float is always exact. Decimal remains the safer choice for financial calculations.

## 2. Rate Revision

The rate card should be stored separately from the calculation logic. For a small co-operative, a JSON or text file is suitable.

When the co-operative revises its rates:
1. An authorised person updates the rate-card file.
2. The new rates are checked and validated.
3. The program loads the revised rates at start-up.
4. Test cases are run to verify the new calculations.
5. The old rate card is retained for auditing and historical payment verification.

Separating rates from the program avoids editing and redistributing the source code for every rate revision.

## 3. Limitations of the Design

- Incorrect or incomplete input data can affect the payment result.
- A simple local program does not automatically provide secure multi-user access or centralised records.
- The program requires input validation, access control, backups, and an audit trail for production use.
- Float and Decimal performance can differ, and the Task 10 timing measurements depend on the computer and test conditions.
- A rate card must be validated before use to prevent incorrect payments.

## 4. Suitability for District-Union Scale

The calculation logic and dictionary rate table can support large numbers of entries because processing each entry takes approximately constant time when the rate is already available.

However, a district union would need more than a basic standalone script. It should use a central database, secure user access, transaction records, backups, audit logs, and controlled rate-card revisions. Batch processing and database indexing would also help manage large datasets.

Therefore, the current design is suitable as a prototype and as a foundation for a larger system, but it requires additional infrastructure before district-wide deployment.

## 5. Alternative: Load the Rate Card from a File

The program can read a JSON file at start-up instead of defining rates inside a Python module.

Example JSON file:

```json
{
  "base_rate": "30.00",
  "fat_step_value": "0.40",
  "snf_step_value": "0.30",
  "reference_fat": "3.5",
  "reference_snf": "8.5",
  "minimum_fat": "2.0",
  "maximum_fat": "7.0"
}
```

The program would use Python's `json` module to read the file and `Decimal` to convert its financial values safely.

### Complexity Analysis

Let `t` be the number of rate-card values and `n` the number of milk entries.

- Start-up reading time: O(t), assuming the file contains `t` values.
- Space for the loaded rate card: O(t).
- Processing entries with a dictionary rate table: O(n) average lookup time for all entries, plus the cost of calculating rates for any new input pairs.
- Editing a separate file is simpler than modifying, testing, and redistributing the program after every rate revision.

For a small rate card, the start-up cost is usually negligible. The file-based approach is more maintainable because authorised rate changes do not require changing the calculation functions.

## 6. Evidence from Experiments

Task 9 tested normal values, standard values, minimum and maximum allowed fat percentages, invalid inputs, and a five-entry total of ₹1,259.50.

Task 10 compared 300, 6,000, and 150,000 payments. Float and Decimal produced identical totals in these tests. The dictionary rate-table approach took 0.084485 seconds compared with 0.317435 seconds for recalculating rates in the recorded run.

These results support separating rate data from calculation logic and reusing rates when input pairs repeat. The measured times are specific to the test environment and should not be treated as guaranteed performance at district scale.

## 7. Test Results

| Test Case | Input (Litres, Fat, SNF) | Expected Rate | Expected Payment | Result |
|---|---|---:|---:|---|
| Standard values | 10, 3.5%, 8.5% | ₹30.00/L | ₹300.00 | PASS |
| Values above standard | 8.5, 4.2%, 8.7% | ₹33.40/L | ₹283.90 | PASS |

Both tests produced the expected results. The program successfully loaded the rate values and calculated payments using Decimal arithmetic.

**Testing note:** The program was tested in OnlineGDB using a temporary Python dictionary containing the same rate values as `rate_card.json`. The committed GitHub version continues to load the rate card from the separate JSON file.

## 8. System Design

The proposed milk-payment calculator uses a modular design in which the rate card is stored separately from the calculation logic.

### System Architecture

```text
        +--------------------------+
        |  Farmer Milk Entry       |
        |  Litres, Fat and SNF     |
        +------------+-------------+
                     |
                     v
        +--------------------------+
        | Input Validation         |
        | Check values and limits  |
        +------------+-------------+
                     |
                     v
        +--------------------------+
        | Load Rate Card           |
        | rate_card.json           |
        +------------+-------------+
                     |
                     v
        +--------------------------+
        | Calculate Rate per Litre |
        | Decimal Arithmetic       |
        +------------+-------------+
                     |
                     v
        +--------------------------+
        | Calculate Farmer Payment|
        | Apply Rounding Rule      |
        +------------+-------------+
                     |
                     v
        +--------------------------+
        | Display Payment Details  |
        | Rate and Amount Payable  |
        +--------------------------+
```

### Design Explanation

1. **Input layer:** Accepts milk quantity, fat percentage, and SNF percentage.
2. **Validation layer:** Rejects invalid quantities and values outside the allowed fat range.
3. **Configuration layer:** Loads the current rate values from `rate_card.json`.
4. **Calculation layer:** Uses Decimal arithmetic to calculate the rate per litre and payment.
5. **Output layer:** Displays the rate and the rounded payment amount.

### Design Justification

This modular design separates configuration, validation, calculation, and output. Rate revisions can be made in the JSON file without modifying the calculation functions. Decimal arithmetic supports reliable decimal-based financial calculations, while a dictionary rate table can reduce repeated rate calculations when the same fat and SNF pairs occur frequently.

For district-union deployment, the design would need a central database, user access controls, audit logs, backups, and additional testing.

## 9. Evidence

The following files were uploaded for Task 11:

1. `README.md` – Contains the final design recommendation, data-type and rounding justification, rate revision method, limitations, district-union scalability analysis, and complexity analysis.
2. `rate_card.json` – Stores the milk rate values separately from the Python calculation logic.
3. `task11.py` – Implements Decimal-based payment calculations, input validation, and rate-card loading.
4. Test results recorded in the README – Documents the two successful tests conducted using OnlineGDB.
5. Task_11_System_Design.png – Screenshot of the system architecture diagram showing the input, validation, rate-card loading, calculation, and output stages.

**Note:** The OnlineGDB tests used a temporary Python dictionary containing the same rate values because the separate JSON file was not loaded directly in that editor.
## Conclusion

I recommend using Decimal for financial calculations, a documented rounding rule for individual farmer payments, and a validated external JSON rate card for easier maintenance. The dictionary rate table can improve performance when many entries share the same fat and SNF values. For district-union deployment, the design should be extended with a secure database, audit records, access control, and backup facilities.
