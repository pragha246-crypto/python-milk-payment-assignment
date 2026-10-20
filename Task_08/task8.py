
# Task 8: Plan the Algorithm Before Coding

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def rate_per_litre(fat, snf):
    """Calculate milk rate per litre."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE
    rate += snf_steps * SNF_STEP_VALUE
    return round(rate, 2)


def payout(litres, fat, snf):
    """Calculate payment for one entry."""
    return round(litres * rate_per_litre(fat, snf), 2)


def read_entry(day):
    """Read and validate one day's milk entry."""
    while True:
        print(f"\nDay {day}")

        try:
            litres = float(input("Enter litres: "))
            fat = float(input("Enter fat percentage: "))
            snf = float(input("Enter SNF percentage: "))

            if litres < 0 or fat < 0 or snf < 0:
                print("Invalid entry: values cannot be negative.")
                continue

            return litres, fat, snf

        except ValueError:
            print("Invalid entry: please enter numeric values. Try again.")


def main():
    total_payment = 0.0

    print("TEN-DAY MILK PAYMENT CALCULATOR")

    for day in range(1, 11):
        litres, fat, snf = read_entry(day)

        rate = rate_per_litre(fat, snf)
        payment = payout(litres, fat, snf)
        total_payment += payment

        print(f"Rate per litre: Rs. {rate:.2f}")
        print(f"Payment: Rs. {payment:.2f}")

    print(f"\nTen-day total payment: Rs. {total_payment:.2f}")


if __name__ == "__main__":
    main()
