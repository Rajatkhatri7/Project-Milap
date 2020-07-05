from menu_item import MenuItem

menu_item1 = MenuItem('Sandwich', 5)
menu_item2 = MenuItem('Chocolate Cake', 4)
menu_item3 = MenuItem('Coffee', 3)
menu_item4 = MenuItem('Orange Juice', 2)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]


for index,menu_item in enumerate(menu_items):
    # Print out in the format '0. Sandwich: $5' for each index
    print(str(index)+". "+menu_item.info())

print('--------------------')

order = int(input('Enter menu item number: '))
selected_menu = menu_items[order]
print('Selected item: ' + selected_menu.name)

# Receive input from the console for no of items
count = int(input("Enter quantity (10% off for 3 or more): "))

# Call the get_total_price method
result = selected_menu.get_total_price(count)

# Output 
print("Your total is $"+str(result))
