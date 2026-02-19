def main():
    revenues = get_revenues()
    print_chart(revenues)


# sample projected revenue values
def get_revenues():
    return [3, 5, 8, 12, 16]


# prints chart
def print_chart(values):
    year = 1

    for amount in values:
        bars = "#" * amount
        print(f"Year {year}: {bars}")
        year += 1


main()