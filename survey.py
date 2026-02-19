def main():
    preferences = get_preferences()
    counts = count_preferences(preferences)
    print_market_share(counts, len(preferences))


# sample survey data (list of choices)
def get_preferences():
    return ["coffee", "tea", "coffee", "soda"]


# dictionary counting (key = product, value = count)
def count_preferences(data):
    counts = {}

    for choice in data:
        if choice in counts:
            counts[choice] = counts[choice] + 1
        else:
            counts[choice] = 1

    return counts


# loops through dictionary keys and calculates percentage of total for each product
def print_market_share(counts, total):
    print("Market Share Summary")

    for product in counts:
        percent = (counts[product] / total) * 100
        print(product, f"{percent:.0f}%")


main()
