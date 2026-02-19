def main():
    revenue = float(input("Initial revenue: "))
    rate = float(input("Growth rate (%): ")) / 100

    project_growth(revenue, rate)


# yearly growth loop
def project_growth(amount, rate):
    print("Year  Revenue")

    year = 1
    for _ in range(10):
        print(year, f"${amount:.2f}")
        amount = amount * (1 + rate)
        year += 1


main()