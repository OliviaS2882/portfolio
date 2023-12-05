print("Welcome to Paws n Cart")
print("__________________________________________________________________________________")  
print("This is your shopping cart:")
print("__________________________________________________________________________________")

items = ""
prices = ""
cart_total = 0.0
done = False    

while (not done):
    print("Would you like to:\n1. Add an item to your cart\n2. Remove an item from your cart\n3. View the total cost of your cart\n4. Checkout")
    selection = input("Enter the number of the option you would like to choose:\n")

    if selection == "1":
        new_item = input("What item would you like to add to your cart?:\n")
        new_price = float(input("How much does the item cost?:\n£"))    
        items += f",{new_item}"
        prices += f",{new_price}"
        cart_total += new_price
        print(f"{new_item} has been successfully added to your cart.\n")
        print("__________________________________________________________________________________\n")
        print("This is your shopping cart:")
        item_list = items.split(',')[1:]  # Splitting items string into a list
        price_list = prices.split(',')[1:]  # Splitting prices string into a list
        for i, item in enumerate(item_list):
            print("{:<30} £{:.2f}".format(item, float(price_list[i])))

    elif selection == "2":
        removed_item = input("Which item would you like to remove?:\n")
        removed_price = float(input("How much does the item cost?:\n£"))
        if removed_item in items:
            items = ",".join(filter(lambda x: x != removed_item, items.split(",")))
            prices = ",".join(filter(lambda x: x != str(removed_price), prices.split(",")))
            cart_total -= removed_price
            print(f"{removed_item} has been successfully removed from your cart.")
            print("__________________________________________________________________________________\n")

    elif selection == "3":
        
        print(f"The total cost of your cart is: £{cart_total: .2f}")
        print("__________________________________________________________________________________\n")

    elif selection == "4":
        print("Thank you for shopping with Paws n Cart")
        print("__________________________________________________________________________________\n")
        done = True

    else:
        print("You have entered an invalid selection.")
        print("__________________________________________________________________________________\n")