
# Task 3: Choose Variables and Name the Constants

# Named constants (UPPER_CASE convention)
BASE_RATE = 30.0
FAT_RATE = 0.40
SNF_RATE = 0.30
MIN_FAT = 3.0
MIN_SNF = 8.0

# Calculate the milk rate using named constants
fat = 4.2
snf = 8.7

fat_steps = int((fat - MIN_FAT) / 0.1)
snf_steps = int((snf - MIN_SNF) / 0.1)

rate_per_litre = BASE_RATE + (fat_steps * FAT_RATE) + (snf_steps * SNF_RATE)

print("MILK RATE CALCULATOR")
print("Base rate:", BASE_RATE)
print("Fat rate:", FAT_RATE)
print("SNF rate:", SNF_RATE)
print("Fat percentage:", fat)
print("SNF percentage:", snf)
print(f"Rate per litre: Rs. {rate_per_litre:.2f}")

# Dynamic typing
value = 10
print("Value:", value, "| Type:", type(value).__name__)
value = "Milk"
print("Value:", value, "| Type:", type(value).__name__)

# Multiple assignment and swapping
a, b = 5, 10
print("Before swapping: a =", a, ", b =", b)
a, b = b, a
print("After swapping: a =", a, ", b =", b)

# Rate revision complexity
print("Using named constants, a rate revision needs changes in one place.")
print("Hard-coded magic numbers may need changes at multiple places.")
