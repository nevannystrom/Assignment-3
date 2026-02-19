def main():
    warehouses = get_warehouses()
    totals = calculate_totals(warehouses)
    print_totals(totals)


# list of warehouse dictionaries
def get_warehouses():
    return [
        {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
        {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}}
    ]


# nested loops: warehouses -> inventory -> products
def calculate_totals(data):
    totals = {}

    for warehouse in data:                       # loop through list
        inventory = warehouse["inventory"]

        for product in inventory:                # loop through dictionary
            amount = inventory[product]

            if product in totals:
                totals[product] = totals[product] + amount
            else:
                totals[product] = amount

    return totals


# print results
def print_totals(totals):
    print("Total Supply Chain Inventory")

    for product in totals:
        print(product, totals[product])


main()