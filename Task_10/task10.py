
# Task 10: Compare Expectations with Execution

from decimal import Decimal
from time import perf_counter

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def rate_per_litre(fat, snf):
    """Calculate the milk rate per litre."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE,
        2,
    )


def create_payments(count):
    """Generate a repeatable set of milk payments."""
    payments = []
    entries = [
        (10, 3.5, 8.5),
        (8.5, 4.2, 8.7),
        (12, 3.1, 8.3),
        (5, 3.5, 8.5),
        (6, 4.0, 8.5),
    ]

    for i in range(count):
        litres, fat, snf = entries[i % len(entries)]
        rate = rate_per_litre(fat, snf)
        payments.append(litres * rate)

    return payments


def measure_float(payments):
    start = perf_counter()
    total = sum(payments)
    elapsed = perf_counter() - start
    return total, elapsed


def measure_decimal(payments):
    # Convert from strings to avoid importing binary float errors.
    decimal_payments = [Decimal(str(p)) for p in payments]

    start = perf_counter()
    total = sum(decimal_payments, Decimal("0.00"))
    elapsed = perf_counter() - start
    return total, elapsed


def compare_rounding(payments):
    # Method 1: round each payment before adding.
    rounded_each = sum(round(p + 1e-9, 2) for p in payments)

    # Method 2: add first, then round the final total.
    rounded_total = round(sum(payments) + 1e-9, 2)

    print("\nROUNDING COMPARISON")
    print(f"Round each payment: Rs. {rounded_each:.2f}")
    print(f"Round final total:  Rs. {rounded_total:.2f}")
    print(f"Difference:         Rs. {abs(rounded_each - rounded_total):.2f}")


def compare_rate_table(count):
    entries = [
        (10, 3.5, 8.5),
        (8.5, 4.2, 8.7),
        (12, 3.1, 8.3),
        (5, 3.5, 8.5),
        (6, 4.0, 8.5),
    ]
    data = [entries[i % len(entries)] for i in range(count)]

    start = perf_counter()
    total_recalculated = 0.0
    for litres, fat, snf in data:
        total_recalculated += litres * rate_per_litre(fat, snf)
    recalc_time = perf_counter() - start

    rate_table = {}
    start = perf_counter()
    total_lookup = 0.0
    for litres, fat, snf in data:
        key = (fat, snf)
        if key not in rate_table:
            rate_table[key] = rate_per_litre(fat, snf)
        total_lookup += litres * rate_table[key]
    lookup_time = perf_counter() - start

    print("\nRATE TABLE COMPARISON")
    print(f"Recalculated total: Rs. {total_recalculated:.2f}")
    print(f"Lookup total:       Rs. {total_lookup:.2f}")
    print(f"Recalculation time: {recalc_time:.6f} seconds")
    print(f"Lookup time:        {lookup_time:.6f} seconds")
    print(f"Unique rate pairs:  {len(rate_table)}")


def main():
    print("TASK 10: FLOAT AND DECIMAL COMPARISON")
    print("-" * 65)

    for count in (300, 6000, 150000):
        payments = create_payments(count)

        float_total, float_time = measure_float(payments)
        decimal_total, decimal_time = measure_decimal(payments)

        difference = abs(
            Decimal(str(float_total)) - decimal_total
        )

        print(f"\nNumber of payments: {count:,}")
        print(f"Float total:   Rs. {float_total:.2f}")
        print(f"Decimal total: Rs. {decimal_total:.2f}")
        print(f"Absolute difference: Rs. {difference:.6f}")
        print(f"Float time:   {float_time:.6f} seconds")
        print(f"Decimal time: {decimal_time:.6f} seconds")

    compare_rounding(create_payments(300))
    compare_rate_table(150000)


if __name__ == "__main__":
    main()
