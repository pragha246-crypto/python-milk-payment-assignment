
# Task 6: Organise the Logic into Functions

BASE_RATE = 30.0
FAT_RATE = 0.40
SNF_RATE = 0.30
REFERENCE_FAT = 3.5
REFERENCE_SNF = 8.5
STEP_SIZE = 0.1


def rate_per_litre(fat, snf):
    """Calculate the milk rate per litre from fat and SNF percentages."""
    fat_steps = round((fat - REFERENCE_FAT) / STEP_SIZE)
    snf_steps = round((snf - REFERENCE_SNF) / STEP_SIZE)
    return BASE_RATE + fat_steps * FAT_RATE + snf_steps * SNF_RATE


def payout(quantity, rate):
    """Return the payment for the supplied milk quantity and rate."""
    return quantity * rate


def ten_day_total(daily_quantities, rate):
    """Calculate the total payment for quantities recorded over ten days."""
    return sum(daily_quantities) * rate


def main():
    """Run sample milk-rate and payment calculations."""
    fat = 4.2
    snf = 8.7
    quantity = 10.0
    daily_quantities = [10.0] * 10

    rate = rate_per_litre(fat, snf)
    payment = payout(quantity, rate)
    ten_day_payment = ten_day_total(daily_quantities, rate)

    print("MILK PAYMENT CALCULATOR")
    print(f"Rate per litre: Rs. {rate:.2f}")
    print(f"Payment for {quantity:.2f} L: Rs. {payment:.2f}")
    print(f"Ten-day payment: Rs. {ten_day_payment:.2f}")


if __name__ == "__main__":
    main()
