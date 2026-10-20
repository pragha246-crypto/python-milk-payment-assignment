
# Task 9: Implement and Test the Calculator

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
REFERENCE_FAT = 3.5
REFERENCE_SNF = 8.5
MIN_FAT = 2.0
MAX_FAT = 7.0


def validate_entry(litres, fat, snf):
    """Validate and convert the three milk-entry values."""
    try:
        litres = float(litres)
        fat = float(fat)
        snf = float(snf)
    except (ValueError, TypeError):
        raise ValueError("All entries must be numeric.")

    if litres <= 0:
        raise ValueError("Milk quantity must be positive.")

    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Fat must be between 2.0 and 7.0.")

    if snf < 0:
        raise ValueError("SNF cannot be negative.")

    return litres, fat, snf


def rate_per_litre(fat, snf):
    """Calculate the milk rate per litre, rounded to two decimals."""
    try:
        fat = float(fat)
        snf = float(snf)
    except (ValueError, TypeError):
        raise ValueError("Fat and SNF must be numeric.")

    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Fat must be between 2.0 and 7.0.")

    if snf < 0:
        raise ValueError("SNF cannot be negative.")

    fat_steps = round((fat - REFERENCE_FAT) / 0.1)
    snf_steps = round((snf - REFERENCE_SNF) / 0.1)

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )
    return round(rate, 2)


def payout(litres, fat, snf):
    """Calculate the farmer's payment, rounded to two decimals."""
    litres, fat, snf = validate_entry(litres, fat, snf)
    return round(litres * rate_per_litre(fat, snf), 2)


def calculate_ten_day_total(payments):
    """Return the sum of individual payments, rounded to two decimals."""
    return round(sum(payments), 2)


if __name__ == "__main__":
    print("MILK PAYMENT CALCULATOR")

    try:
        litres = input("Enter milk quantity (L): ")
        fat = input("Enter fat percentage: ")
        snf = input("Enter SNF percentage: ")

        rate = rate_per_litre(fat, snf)
        payment = payout(litres, fat, snf)

        print(f"Rate per litre: Rs. {rate:.2f}")
        print(f"Payment: Rs. {payment:.2f}")

    except ValueError as error:
        print("Invalid entry:", error)
