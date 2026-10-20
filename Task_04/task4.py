
# Task 4: Write Correct Expressions
import math

# Named constants
BASE_RATE = 30.0
FAT_RATE = 0.40
SNF_RATE = 0.30
REFERENCE_FAT = 3.5
REFERENCE_SNF = 8.5
STEP_SIZE = 0.1

# Input values
fat = 4.2
snf = 3.1
quantity = 10.0

# Correct step calculations
fat_steps = round((fat - REFERENCE_FAT) / STEP_SIZE)
snf_steps = round((snf - REFERENCE_SNF) / STEP_SIZE)

# Rate and amount
rate_per_litre = BASE_RATE + fat_steps * FAT_RATE + snf_steps * SNF_RATE
amount = rate_per_litre * quantity

print("TASK 4: WRITE CORRECT EXPRESSIONS")
print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print(f"Rate per litre: Rs. {rate_per_litre:.2f}")
print(f"Amount for {quantity:.1f} litres: Rs. {amount:.2f}")

# Compare round(), int(), and math.floor()
value = (4.2 - 3.5) / 0.1
print("\nROUNDING COMPARISON")
print("Raw value:", repr(value))
print("round(value):", round(value))
print("int(value):", int(value))
print("math.floor(value):", math.floor(value))

negative_value = -1.5
print("\nNEGATIVE VALUE COMPARISON")
print("round(-1.5):", round(negative_value))
print("int(-1.5):", int(negative_value))
print("math.floor(-1.5):", math.floor(negative_value))

# Three unexpected results
print("\nUNEXPECTED RESULTS")
print("1. 0.1 + 0.2 =", 0.1 + 0.2)
print("2. (4.2 - 3.5) / 0.1 =", repr(value))
print("3. -7 // 2 =", -7 // 2)

# Operator precedence and associativity
print("\nOPERATOR PRECEDENCE")
print("-2 ** 2 =", -2 ** 2)
print("(-2) ** 2 =", (-2) ** 2)

# Comparison chaining and Boolean operators
print("\nCOMPARISONS")
print("2.0 <= fat <= 7.0:", 2.0 <= fat <= 7.0)
print("fat >= 2.0 and fat <= 7.0:", fat >= 2.0 and fat <= 7.0)

# Compare step-count methods for fat=4.2 and SNF=3.1
print("\nSTEP METHOD COMPARISON")
for method_name, fat_count, snf_count in [
    ("round", round((4.2 - 3.5) / 0.1), round((3.1 - 8.5) / 0.1)),
    ("int", int((4.2 - 3.5) / 0.1), int((3.1 - 8.5) / 0.1)),
    ("floor", math.floor((4.2 - 3.5) / 0.1),
     math.floor((3.1 - 8.5) / 0.1))
]:
    rate = BASE_RATE + fat_count * FAT_RATE + snf_count * SNF_RATE
    print(f"{method_name}: fat steps={fat_count}, SNF steps={snf_count}, rate=Rs. {rate:.2f}")

print("\nTime complexity: O(1) for each calculation.")
print("Space complexity: O(1) for the fixed calculations.")
