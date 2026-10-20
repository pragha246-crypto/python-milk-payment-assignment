
# Task 11: Recommend and Defend the Final Design

import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


RATE_FILE = Path(__file__).with_name("rate_card.json")
PAISE = Decimal("0.01")


def load_rate_card():
    """Load and validate the rate card from the JSON file."""
    with RATE_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    required_keys = [
        "base_rate",
        "fat_step_value",
        "snf_step_value",
        "reference_fat",
        "reference_snf",
        "minimum_fat",
        "maximum_fat",
    ]

    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing rate-card value: {key}")

    rates = {key: Decimal(str(data[key])) for key in required_keys}

    if rates["minimum_fat"] > rates["maximum_fat"]:
        raise ValueError("Invalid fat limits.")

    if rates["fat_step_value"] < 0 or rates["snf_step_value"] < 0:
        raise ValueError("Rate step values cannot be negative.")

    return rates


def rate_per_litre(fat, snf, rates):
    """Calculate the rate using Decimal arithmetic."""
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))

    if not rates["minimum_fat"] <= fat <= rates["maximum_fat"]:
        raise ValueError("Fat must be between 2.0 and 7.0.")

    if snf < 0:
        raise ValueError("SNF cannot be negative.")

    fat_steps = ((fat - rates["reference_fat"]) / Decimal("0.1"))
    snf_steps = ((snf - rates["reference_snf"]) / Decimal("0.1"))

    # The inputs are expected in 0.1% increments.
    if fat_steps != fat_steps.to_integral_value():
        raise ValueError("Fat must use 0.1% increments.")

    if snf_steps != snf_steps.to_integral_value():
        raise ValueError("SNF must use 0.1% increments.")

    rate = (
        rates["base_rate"]
        + fat_steps * rates["fat_step_value"]
        + snf_steps * rates["snf_step_value"]
    )

    return rate.quantize(PAISE, rounding=ROUND_HALF_UP)


def payout(litres, fat, snf, rates):
    """Calculate the rounded payment for one farmer entry."""
    litres = Decimal(str(litres))

    if litres <= 0:
        raise ValueError("Milk quantity must be positive.")

    rate = rate_per_litre(fat, snf, rates)
    return (litres * rate).quantize(PAISE, rounding=ROUND_HALF_UP)


def main():
    try:
        rates = load_rate_card()
        print("MILK PAYMENT CALCULATOR")
        print("Rate card loaded successfully.")

        litres = input("Enter milk quantity (L): ")
        fat = input("Enter fat percentage: ")
        snf = input("Enter SNF percentage: ")

        payment = payout(litres, fat, snf, rates)
        rate = rate_per_litre(fat, snf, rates)

        print(f"Rate per litre: Rs. {rate:.2f}")
        print(f"Payment: Rs. {payment:.2f}")

    except (ValueError, TypeError, OSError, json.JSONDecodeError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
