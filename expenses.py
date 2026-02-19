def main():
    expenses = get_expenses()
    grand_total = print_report(expenses)

    print(f"Grand Total: ${grand_total:.2f}")


# sample expense dictionary
def get_expenses():
    return {
        "Travel": [500, 200],
        "Meals": [40, 60, 30],
        "Supplies": [100]
    }


# loops through categories and adds amounts
def print_report(data):
    grand_total = 0

    for category in data:                    # loop through dictionary keys
        category_total = 0

        for amount in data[category]:        # nested loop through list
            category_total = category_total + amount

        print(f"{category}: ${category_total:.2f}")
        grand_total = grand_total + category_total

    return grand_total


main()
