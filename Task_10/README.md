# Task 10 – Compare Expectations with Execution

## Aim
To compare floating-point and Decimal arithmetic, measure calculation time, examine rounding methods, and analyse the use of a dictionary-based rate table.

## 1. Float and Decimal Comparison
The calculator will calculate totals for 300, 6,000, and 150,000 payments using both `float` and `Decimal`.

Expected behaviour:
- `float` may introduce small binary floating-point representation errors.
- `Decimal` supports exact decimal arithmetic when initialized from strings.
- The difference between the totals will be measured and recorded.

## 2. Execution Time
The `time.perf_counter()` function will measure the time required for each calculation size. The measured times will be recorded in seconds.

## 3. Rounding Comparison
Two approaches will be compared:
1. Round each individual payment to two decimal places, then add the payments.
2. Add the unrounded payments, then round the final total to two decimal places.

For bank payments, rounding each individual payment to the nearest paisa before summing is appropriate when each payment is separately payable and recorded.

## 4. Dictionary-Based Rate Table
A dictionary can store the calculated rate for each unique `(fat, snf)` pair. Subsequent entries with the same pair can retrieve the rate using an average O(1) dictionary lookup instead of recalculating it.

- Recalculation: performs the rate calculation for every entry.
- Dictionary lookup: reuses a previously calculated rate.
- Extra space: O(k), where k is the number of unique `(fat, snf)` pairs.

## 5. Evidence
The completed Python program, measured totals, execution times, rounding comparison, and dictionary lookup analysis will be added after testing.

## Conclusion
The experiment will establish the numerical differences and performance characteristics of `float`, `Decimal`, and dictionary-based rate lookup using observed results.

## 6. Observed Results and Comparison

### A. Float and Decimal Totals

| Number of payments | Float total (₹) | Decimal total (₹) | Difference (₹) |
|---:|---:|---:|---:|
| 300 | 75,570.00 | 75,570.00 | 0.00 |
| 6,000 | 1,511,400.00 | 1,511,400.00 | 0.00 |
| 150,000 | 37,785,000.00 | 37,785,000.00 | 0.00 |

### B. Measured Execution Times

| Number of payments | Float time (seconds) | Decimal time (seconds) |
|---:|---:|---:|
| 300 | 0.000920 | 0.000105 |
| 6,000 | 0.000280 | 0.001420 |
| 150,000 | 0.002560 | 0.034265 |

The measured times vary with the computer and system conditions. In this experiment, Decimal summation took longer for 6,000 and 150,000 payments. For 300 payments, Decimal summation was faster in the recorded run. These measurements time the summation itself; Decimal conversion is performed before its timer starts.

### C. Rounding Comparison

| Method | Total (₹) |
|---|---:|
| Round each payment, then add | 75,570.00 |
| Add payments, then round total | 75,570.00 |
| Difference | 0.00 |

Both methods produced the same result because the generated payments were already expressed to two decimal places. When each payment is separately payable, rounding each payment to the nearest paisa before adding is appropriate. If only one combined payment is made, rounding the final total may be appropriate, depending on the payment rules.

### D. Rate Table Comparison

| Method | Total (₹) | Execution time (seconds) |
|---|---:|---:|
| Recalculate the rate for each entry | 37,785,000.00 | 0.317435 |
| Use a dictionary rate table | 37,785,000.00 | 0.084485 |

The dictionary stored four unique `(fat, snf)` pairs. Its lookup approach was faster in this run because repeated pairs reused previously calculated rates.

### E. Analysis and Reasons for Differences

The float and Decimal totals agreed for all three test sizes, with an observed difference of ₹0.00. This happened because the generated payment values were already rounded to two decimal places and were converted to Decimal through strings.

Float uses binary floating-point representation, which can introduce small precision errors for some decimal values. Decimal is designed for decimal arithmetic and is useful for financial calculations. However, Decimal is not automatically faster than float.

The rate table reduced the measured execution time from 0.317435 seconds to 0.084485 seconds. For `n` entries and `k` unique `(fat, snf)` pairs, recalculation requires O(n) rate calculations, while the dictionary approach requires O(k) rate calculations and O(n) average-time lookups. The dictionary uses O(k) additional space. Both approaches still require O(n) time to process all entries.

### Conclusion

The experiment showed identical totals for float and Decimal in the tested data. The rounding methods also produced identical totals. The dictionary rate table was faster for the repeated test entries, demonstrating that caching repeated calculations can improve performance. The results support using Decimal for financial precision and a dictionary when many entries share the same rate inputs.

## Evidence

The following files were uploaded for Task 10:

1. `task10.py` – Python source code implementing float and Decimal comparisons, execution-time measurements, rounding comparisons, and dictionary-based rate-table analysis.
2. `Task_10_Output.png` – Screenshot of the program output showing measured totals, execution times, rounding results, and rate-table comparison.
