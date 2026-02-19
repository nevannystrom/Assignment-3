def main():
    customers = get_customers()
    bronze, silver, gold = count_tiers(customers)

    print("Loyalty Tier Summary")
    print("Bronze:", bronze)
    print("Silver:", silver)
    print("Gold:", gold)


# sample customer purchase totals
def get_customers():
    return {
        "Alice": 1200,
        "Bob": 600,
        "Charlie": 5200,
        "Dana": 980,
        "Evan": 7500
    }


# classify each customer
def count_tiers(data):
    bronze = 0
    silver = 0
    gold = 0

    for name in data:
        total = data[name]

        if total < 1000:
            bronze += 1
        elif total < 5000:
            silver += 1
        else:
            gold += 1

    return bronze, silver, gold


main()