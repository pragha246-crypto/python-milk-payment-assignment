# Task 12 – Re-evaluate and Adapt the Design

## Aim
To evaluate the original milk-payment calculator and adapt it to support two-decimal analyser readings, seasonal rates, and a ten-day supply bonus.

## A. Impact Analysis 

### Changes from the Original Problem

The original calculator used a fixed base rate of ₹30.00, a fat-step value of ₹0.40, and analyser values expressed using one decimal place in the test examples. The revised problem introduces two-decimal fat and SNF readings, an April–June seasonal rate card, a revised fat-step value, and a bonus for supplying more than 500 litres in ten days.

### Affected Constants, Expressions and Functions

- `BASE_RATE` must support seasonal values: ₹30.00 normally and ₹32.00 from April to June.
- `FAT_STEP_VALUE` changes from ₹0.40 to ₹0.45 during April–June.
- The fat and SNF calculation must handle two-decimal readings consistently.
- A season-selection function is needed to select the correct rate card.
- A separate bonus function is needed to calculate the ten-day bonus.
- The payment calculation must use a consistent decimal rounding rule.

### Effect of Two-Decimal Readings

The tariff increments remain defined in 0.1 percentage-point steps. Therefore, the revised design will round analyser readings to the nearest 0.1 percentage point using `ROUND_HALF_UP` before calculating tariff steps. This avoids silently treating a partial step as a full step.

For example, a fat reading of 4.23% becomes 4.2%. Relative to the reference fat of 3.5%, this gives:

Fat steps = (4.2 − 3.5) / 0.1 = 7 steps.

The rounding policy must be documented because a different tariff rule could instead permit fractional steps.

## B. Evaluation of the Original Design 

The original design is modular and remains a useful foundation, but its fixed constants cannot represent seasonal changes or the bonus requirement.

For a reading of 4.2% fat and 8.7% SNF, the original formula gives:

- Fat steps = (4.2 − 3.5) / 0.1 = 7
- SNF steps = (8.7 − 8.5) / 0.1 = 2

Under the original rates:

Rate = 30.00 + (7 × 0.40) + (2 × 0.30) = ₹33.40 per litre.

Under the April–June rates:

Rate = 32.00 + (7 × 0.45) + (2 × 0.30) = ₹35.75 per litre.

The original functions can be retained conceptually, but the constants must be selected by season and a new function must calculate the ten-day bonus. The original module is therefore suitable for modification rather than complete replacement.

## C. Adaptation or Redesign 

The revised design will:

1. Select the rate card using the season.
2. round two-decimal analyser readings to the nearest 0.1 percentage point using a documented rule.
3. Calculate the rate using the selected seasonal constants.
4. Calculate each farmer's payment using Decimal arithmetic and round to two decimal places.
5. Add a bonus of ₹0.50 per litre only when ten-day supply exceeds 500 litres.

The implementation is stored in `task12.py`, with the rate configuration stored separately in `rate_cards.json`.

## Test Results and Evidence

### 1. Seasonal Rate Tests

Test readings: Fat = 4.23%, SNF = 8.72%, milk quantity = 10 litres.

The tariff readings are rounded to 4.2% fat and 8.7% SNF before calculating the rate.

| Test | Season | Base Rate | Fat Step Value | Calculated Rate | Payment |
|---|---|---:|---:|---:|---:|
| 1 | Normal | ₹30.00 | ₹0.40 | ₹33.40/L | ₹334.00 |
| 2 | April–June | ₹32.00 | ₹0.45 | ₹35.75/L | ₹357.50 |

**Calculation for the normal season**

Fat steps = (4.2 − 3.5) / 0.1 = 7

SNF steps = (8.7 − 8.5) / 0.1 = 2

Rate = ₹30.00 + (7 × ₹0.40) + (2 × ₹0.30) = ₹33.40/L

Payment = 10 × ₹33.40 = ₹334.00

**Calculation for April–June**

Rate = ₹32.00 + (7 × ₹0.45) + (2 × ₹0.30) = ₹35.75/L

Payment = 10 × ₹35.75 = ₹357.50

### 2. Ten-Day Bonus Boundary Tests

| Ten-Day Supply | Expected Bonus | Result |
|---:|---:|---|
| 499 L | ₹0.00 | PASS |
| 500 L | ₹0.00 | PASS |
| 501 L | ₹250.50 | PASS |
| 600 L | ₹300.00 | PASS |

The results confirm that the bonus is awarded only when total supply is strictly greater than 500 litres.

### 3. Evaluation and Final Decision

The original fixed-rate design cannot directly represent seasonal rate changes or ten-day bonuses. The revised design selects rates by season, uses Decimal arithmetic for financial calculations, and implements the bonus separately.

The tests support modifying the original modular design instead of replacing it completely. The main trade-off is that rounding analyser readings to 0.1 percentage-point increments discards some measurement precision. This rule should be confirmed by the milk co-operative.

### 4. Evidence Files

- `README.md` – impact analysis, evaluation, adaptation, calculations, test results, and final defence.
- `rate_cards.json` – seasonal rates and bonus settings.
- `task12.py` – revised implementation.
- `Task_12_Output.png` – Seasons test screenshot.

**Result:** The revised design supports seasonal rates, two-decimal analyser readings, and a ten-day bonus rule through separate, reusable functions.
