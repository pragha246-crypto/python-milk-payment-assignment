
# Task 7: Test importing the milkrate module

import milkrate

print("TESTING IMPORTED MILKRATE MODULE")
print()

for litres, fat, snf in [
    (10, 3.5, 8.5),
    (8.5, 4.2, 8.7),
    (12, 3.1, 8.3),
]:
    rate = milkrate.rate_per_litre(fat, snf)
    payment = milkrate.payout(litres, fat, snf)

    print(
        f"{litres:5} L fat {fat} snf {snf} "
        f"rate {rate:6.2f} pay {payment:8.2f}"
    )
