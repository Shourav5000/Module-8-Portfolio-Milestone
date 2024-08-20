# Class representing an item to be purchased
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        # Initialize item attributes with default values
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # Method to print the cost of the item
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity  # Calculate total cost
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")  # Output item cost


# Class representing a shopping cart
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # Initialize cart attributes with default values
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []  # List to store items in the cart

    # Method to add an item to the cart
    def add_item(self, item):
        self.cart_items.append(item)

    # Method to remove an item from the cart by name
    def remove_item(self, item_name):
        found = False  # Flag to check if the item is found
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)  # Remove item from cart
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")  # Message if item not found

    # Method to modify an item in the cart
    def modify_item(self, item):
        found = False  # Flag to check if the item is found
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                # Modify the item only if new values are provided
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")  # Message if item not found

    # Method to get the total number of items in the cart
    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity  # Sum up quantities
        return total_quantity

    # Method to get the total cost of all items in the cart
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity  # Sum up total costs
        return total_cost

    # Method to print the total cost of the shopping cart
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")  # Message if cart is empty
        else:
            for item in self.cart_items:
                item.print_item_cost()  # Print cost for each item
            print(f"\nTotal: ${self.get_cost_of_cart()}")  # Print total cost

    # Method to print descriptions of items in the cart
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}")  # Print item name (description)


# Helper function to safely get a float input from the user
def get_float_input(prompt):
    while True:
        value = input(prompt)
        if value == '0':  # Allow skipping with '0'
            return 0.0
        try:
            return float(value)  # Attempt to convert to float
        except ValueError:
            print("Invalid input. Please enter a numeric value.")  # Error message and retry


# Function to display the menu and interact with the shopping cart
def print_menu(cart):
    menu = """MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option:"""
    option = ''
    while option != 'q':
        print(menu)
        option = input()  # Get user input for menu option
        if option == 'a':
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            price = get_float_input("Enter the item price:\n")
            quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(name, price, quantity)  # Create a new item
            cart.add_item(item)  # Add item to the cart
        elif option == 'r':
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)  # Remove item from cart by name
        elif option == 'c':
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity (0 to skip):\n"))
            item = ItemToPurchase(name, 0, quantity)  # Create an item with the new quantity
            cart.modify_item(item)  # Modify item in the cart
        elif option == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()  # Print descriptions of items in the cart
        elif option == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()  # Print the total cost of the cart
        elif option != 'q':
            print("Choose an option:")


# Main function to run the shopping cart program
if __name__ == "__main__":
    # Get customer name and date
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    # Create a new shopping cart
    shopping_cart = ShoppingCart(customer_name, current_date)
    # Call the print_menu function to start interacting with the cart
    print_menu(shopping_cart)
