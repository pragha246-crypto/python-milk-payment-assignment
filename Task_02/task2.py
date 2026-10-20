
# Task 2: Explore Values and Types in the Interpreter

from decimal import Decimal

# 1. Explore data types
print("DATA TYPES")
print(type(10))
print(type(10.0))
print(type("10"))
print(type(True))
print(type([10, 8.5]))

# 2. Explore division operators
print("\nDIVISION OPERATORS")
print("7 / 2 =", 7 / 2)
print("7 // 2 =", 7 // 2)
print("7 % 2 =", 7 % 2)
print("-7 // 2 =", -7 // 2)

# 3. Floating-point arithmetic
print("\nFLOATING-POINT ARITHMETIC")
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)

# 4. Decimal arithmetic
print("\nDECIMAL ARITHMETIC")
print("Decimal addition:", Decimal("0.1") + Decimal("0.2"))
print("Decimal amount:", Decimal("33.40") * 1000)

# 5. Integer-paise method
print("\nINTEGER-PAISE METHOD")
total_paise = (1000 * 3340) + (3 * 10)
print("Total paise:", total_paise)
print("Total rupees:", f"Rs. {total_paise / 100:.2f}")
