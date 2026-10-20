
# Task 9: Automated Tests Using Assertions

from task9 import rate_per_litre, payout, calculate_ten_day_total


def run_tests():
    test_results = []

    def check(name, expected, actual):
        assert expected == actual, (
            f"{name} failed: expected {expected}, got {actual}"
        )
        test_results.append((name, expected, actual, "PASS"))

    # Normal and boundary tests
    check("Standard values", (30.00, 300.00),
          (rate_per_litre(3.5, 8.5), payout(10, 3.5, 8.5)))

    check("Fat and SNF above standard", (33.40, 283.90),
          (rate_per_litre(4.2, 8.7), payout(8.5, 4.2, 8.7)))

    check("Fat and SNF below standard", (27.80, 333.60),
          (rate_per_litre(3.1, 8.3), payout(12, 3.1, 8.3)))

    check("Minimum allowed fat", 24.00, rate_per_litre(2.0, 8.5))
    check("Maximum allowed fat", 44.00, rate_per_litre(7.0, 8.5))

    # Invalid inputs
    invalid_cases = [
        ("Text quantity", ("abc", 3.5, 8.5)),
        ("Negative quantity", (-5, 3.5, 8.5)),
        ("Fat below minimum", (10, 1.9, 8.5)),
        ("Fat above maximum", (10, 7.1, 8.5)),
    ]

    for name, values in invalid_cases:
        try:
            payout(*values)
        except ValueError:
            test_results.append((name, "ValueError", "ValueError", "PASS"))
        else:
            raise AssertionError(f"{name} failed: expected ValueError")

    # Five entries calculated by hand
    entries = [
        (10, 3.5, 8.5),   # Rs. 300.00
        (8.5, 4.2, 8.7),  # Rs. 283.90
        (12, 3.1, 8.3),   # Rs. 333.60
        (5, 3.5, 8.5),    # Rs. 150.00
        (6, 4.0, 8.5),   # Rs. 192.00
    ]

    payments = [payout(*entry) for entry in entries]
    check("Five-entry total", 1259.50, calculate_ten_day_total(payments))

    print("TASK 9: TEST RESULTS")
    print("-" * 75)
    print(f"{'Test case':<30} {'Expected':<20} {'Actual':<20} {'Status'}")
    print("-" * 75)

    for name, expected, actual, status in test_results:
        print(f"{name:<30} {str(expected):<20} {str(actual):<20} {status}")

    print("-" * 75)
    print(f"All {len(test_results)} tests passed.")


if __name__ == "__main__":
    run_tests()
