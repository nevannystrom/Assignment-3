def main():
    sales = get_sales()
    leaderboard = build_leaderboard(sales)
    print_leaderboard(leaderboard)


# sample sales dictionary
def get_sales():
    return {"Alice": 5000, "Bob": 7000, "Carol": 3000}


# commission function
def calculate_commission(amount):
    return amount * 0.10


# create list of (name, commission) and sort highest first
def build_leaderboard(sales):
    results = []

    for name in sales:
        comm = calculate_commission(sales[name])
        results.append([name, comm])

    results.sort(key=lambda x: x[1], reverse=True) # lambda function to sort by commission amount, highest first
    return results


# print ranking
def print_leaderboard(data):
    rank = 1

    for entry in data:
        print(f"{rank}. {entry[0]} - ${entry[1]:.2f}")
        rank += 1


main()
