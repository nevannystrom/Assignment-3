def main():
    prices = collect_prices()

    total = get_total(prices)
    count = len(prices)
    average = get_average(total, count)

    print(f"Items: {count}")
    print(f"Total: ${total:.2f}")
    print(f"Average: ${average:.2f}")


# keeps asking for prices until user enters 0
def collect_prices():
    items = []

    while True:
        price = float(input("Enter price (0 to stop): "))

        if price == 0:
            return items
        elif price > 0:
            items.append(price)
        else:
            print("Invalid price.")


# adds all numbers in list
def get_total(values):
    total = 0
    for v in values:
        total += v
    return total


# prevents divide by zero
def get_average(total, count):
    if count == 0:
        return 0
    return total / count


main()
