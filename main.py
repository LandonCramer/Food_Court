

def show_menu():
    print("--- De Anza Food Court---")
    print("Please Choose one from the menu:")
    print("1. De Anza Burger  - $5.25")
    print("2. Bacon Cheese.   - $5.75")
    print("3. Mushroom Swiss  - $5.95")
    print("4. Western Burger  - $5.95")
    print("5. Don Cali Burger - $5.95")
    print("6. Exit")
    
def get_valid_input(prompt, min, max):
    pass

def take_orders(prices):
    """Presents menue return dic mapping item number to quantity ordered"""
    quantities = {i:0 for i in prices}
    while True:
        show_menu()
        choice = get_valid_input("Enter your choice (1-6): ", 1, 6)
        
    
def main():
    menu = {
        1: "De Anza Burger", 
        2: "Bacon Cheese",
        3: "Mushroom Swiss",
        4: "Western Burger",
        5: "Don Cali Burger"
    }
    prices = {
        1: 5.25,
        2: 5.75,
        3: 5.95,
        4: 5.95,
        5: 5.95
    }
        
    quantities = take_orders(prices)

if __name__ == "__main__":
    main()