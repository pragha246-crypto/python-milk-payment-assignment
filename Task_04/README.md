# Task 4: Write Correct Expressions

## Aim
To write correct Python expressions for calculating fat steps, SNF steps, milk rate per litre, and payment amount.

## Topics Covered
- Operator precedence and associativity
- Floating-point precision and `round()`
- Differences between `round()`, `int()`, and `math.floor()`
- Comparison chaining and Boolean operators
- Unexpected expression results and their explanations
- Time and space complexity

## 1. Operator Precedence and Associativity

Python evaluates expressions according to operator precedence. For example, `-2 ** 2` evaluates to `-4` because exponentiation occurs before unary negation, whereas `(-2) ** 2` evaluates to `4`.

## 2. Floating-Point Precision

Binary floating-point numbers cannot represent some decimal fractions exactly. Therefore, `0.1 + 0.2` produces approximately `0.30000000000000004`, rather than exactly `0.3`.

## 3. Three Unexpected Results

1. **Floating-point addition:** `0.1 + 0.2` gives approximately `0.30000000000000004` because decimal fractions may not have exact binary representations.
2. **Fat-step calculation:** `(4.2 - 3.5) / 0.1` may produce a value slightly different from `7` due to floating-point precision. This can affect truncation with `int()`.
3. **Floor division with negative values:** `-7 // 2` returns `-4`, because floor division rounds down toward negative infinity rather than toward zero.

## 4. Comparison of Rounding Methods

- `round(x)` rounds to the nearest integer; exact halfway cases use Python's ties-to-even rule.
- `int(x)` truncates the fractional part toward zero.
- `math.floor(x)` returns the greatest integer less than or equal to `x`.

For example, for `x = -1.5`, `round(x)` returns `-2`, `int(x)` returns `-1`, and `math.floor(x)` returns `-2`.

## 5. Comparison Chaining

Python supports expressions such as `2.0 <= fat <= 7.0`. This checks both comparisons and is equivalent to `fat >= 2.0 and fat <= 7.0` for this case.

## 6. Rate-Revision Complexity

Using named constants makes rate revisions easier because each rate can be updated in one place. Hard-coded values scattered across a program may require multiple edits and increase the risk of mistakes.

## 7. Time and Space Complexity

The fixed calculations in this program take **O(1) time** and **O(1) space**. The comparison loop has three fixed iterations, so its total complexity is also O(1).

## 8. Evidence
The Python program, output screenshot, and explanations will be added after testing the expressions against the assignment requirements.
