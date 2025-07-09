# define the menu of restaurant

menu={
    "VegBurger":70,
    "VegCheese":90,
    "VegPeriperi":140,
    "Fries":100,
    "VeggieWrap":110,
    "Pizza":200
}
# Greet
print("WelCome To CRISPIE CRUNCHIE CAFE")
print("VegBurger:Rs70\nVegCheese:Rs90\nVegPeriperi:Rs140\nFries:Rs100\nVeggieWrap:Rs110\nPizza:Rs200")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order!")

else:
    print(f"Ordered item{item_1} not available yet!")


another_order = input("Do you want to add another item? lo(Yes/No)")

if another_order == "Yes":
    item_2 = input("Enter your second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order!")
    else:
        print(f"Orederd item {item_2} not available yet!")


print(f"---The Total Amount Of Item To Pay is Rs {order_total}---")
print("  ---Thank You For Visiting !--- \n     ---Have a Good Day !---")

        