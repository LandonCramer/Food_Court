

def show_menu():
    print("--- De Anza Food Court---")
    print("Please Choose one from the menu:")
    print("1. De Anza Burger  - $5.25")
    print("2. Bacon Cheese.   - $5.75")
    print("3. Mushroom Swiss  - $5.95")
    print("4. Western Burger  - $5.95")
    print("5. Don Cali Burger - $5.95")
    print("6. Exit")
    
def main():

    menue = {
        1: "De Anza Burger", 
        2: "Bacon Cheese",
        3: "Mushroom Swiss",
        4: "Western Burger",
        5: "Don Cali Burger"
    }
    price = {
        1: 5.25,
        2: 5.75,
        3: 5.95,
        4: 5.95,
        5: 5.95
    }
        
    quantities = take_orders(price):
        pass