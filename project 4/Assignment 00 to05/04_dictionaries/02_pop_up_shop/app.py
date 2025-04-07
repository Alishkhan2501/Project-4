
def main():
    fruit_prices = {
        'apple': 1.5,
        'durian': 10.0,
        'jackfruit': 5.0,
        'kiwi': 2.0,
        'rambutan': 3.5,
        'mango': 2.5
    }
    
    total_cost = 0
    
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want to buy?: "))
        total_cost += quantity * price
    
    print(f"Your total is ${total_cost:.2f}")

if __name__ == '__main__':
    main()







