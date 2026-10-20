import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

RATE_FILE = Path(__file__).with_name("rate_cards.json")
PAISE = Decimal("0.01")


def load_rate_cards():
    """Load seasonal rates and bonus settings from JSON."""
    with RATE_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def round_reading(value, step):
    """Round a reading to the nearest tariff step."""
    value = Decimal(str(value))
    step = Decimal(str(step))
    steps = (value / step).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )
    return steps * step


def select_rate_card(season, cards):
    """Select the rate card for the chosen season."""
    if season.lower() in ("april-june", "april_june"):
        return cards["april_june"]
    if season.lower() == "normal":
        return cards["normal"]
    raise ValueError("Season must be normal or april-june.")


def rate_per_litre(fat, snf, rate_card, reading_step):
    """Calculate the rate using the selected seasonal rate card."""
    fat = round_reading(fat, reading_step)
    snf = round_reading(snf, reading_step)

    reference_fat = Decimal(rate_card["reference_fat"])
    reference_snf = Decimal(rate_card["reference_snf"])
    step = Decimal(str(reading_step))

    fat_steps = (fat - reference_fat) / step
    snf_steps = (snf - reference_snf) / step

    rate = (
        Decimal(rate_card["base_rate"])
        + fat_steps * Decimal(rate_card["fat_step_value"])
        + snf_steps * Decimal(rate_card["snf_step_value"])
    )
    return rate.quantize(PAISE, rounding=ROUND_HALF_UP)


def farmer_payment(litres, fat, snf, rate_card, reading_step):
    """Calculate one farmer's payment."""
    litres = Decimal(str(litres))
    if litres <= 0:
        raise ValueError("Milk quantity must be positive.")

    rate = rate_per_litre(fat, snf, rate_card, reading_step)
    payment = (litres * rate).quantize(
        PAISE, rounding=ROUND_HALF_UP
    )
    return rate, payment


def ten_day_bonus(total_litres, cards):
    """Give the bonus only when supply exceeds the threshold."""
    total_litres = Decimal(str(total_litres))
    threshold = Decimal(cards["bonus_threshold_litres"])
    bonus_rate = Decimal(cards["bonus_per_litre"])

    if total_litres < 0:
        raise ValueError("Total milk quantity cannot be negative.")

    if total_litres > threshold:
        return (total_litres * bonus_rate).quantize(
            PAISE, rounding=ROUND_HALF_UP
        )
    return Decimal("0.00")


def main():
    try:
        cards = load_rate_cards()
        season = input("Enter season (normal/april-june): ").strip()
        rate_card = select_rate_card(season, cards)

        litres = input("Enter milk quantity (L): ")
        fat = input("Enter fat percentage: ")
        snf = input("Enter SNF percentage: ")

        rate, payment = farmer_payment(
            litres, fat, snf, rate_card, cards["reading_step"]
        )

        print(f"Rate per litre: Rs. {rate:.2f}")
        print(f"Farmer payment: Rs. {payment:.2f}")

        total_litres = input("Enter total ten-day supply (L): ")
        bonus = ten_day_bonus(total_litres, cards)
        print(f"Ten-day bonus: Rs. {bonus:.2f}")
        print(f"Total including bonus: Rs. {payment + bonus:.2f}")

    except (ValueError, TypeError, KeyError, OSError,
            json.JSONDecodeError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
