
# Task 5: Read Input and Convert Types

def convert_number(text):
    """Convert a valid numeric string into a float."""
    text = text.strip()

    if not text:
        raise ValueError("Input cannot be empty")

    # Accept decimal points, but reject comma decimal notation.
    try:
        return float(text)
    except ValueError:
        raise ValueError("Please enter a valid number, such as 8.5")


print("MILK PAYMENT INPUT")
fat_text = input("Enter fat percentage: ")
snf_text = input("Enter SNF percentage: ")
quantity_text = input("Enter milk quantity (L): ")

try:
    fat = convert_number(fat_text)
    snf = convert_number(snf_text)
    quantity = convert_number(quantity_text)

    if fat < 0 or snf < 0 or quantity < 0:
        raise ValueError("Values cannot be negative")

    print("\nFORMATTED RESULTS")
    print(f"{'Fat percentage:':<22}{fat:8.2f}")
    print(f"{'SNF percentage:':<22}{snf:8.2f}")
    print(f"{'Milk quantity (L):':<22}{quantity:8.2f}")

except ValueError as error:
    print("Invalid input:", error)

# Demonstrate how different entries behave
print("\nINPUT CONVERSION EXAMPLES")
for example in ["8.5", "8,5", "eight"]:
    try:
        result = convert_number(example)
        print(f"{example!r:<10} -> {result:.2f}")
    except ValueError:
        print(f"{example!r:<10} -> Invalid number")
