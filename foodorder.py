from menu_item import MenuItem

menu_item1 = MenuItem('Sandwich', 5)
menu_item2 = MenuItem('Chocolate Cake', 4)
menu_item3 = MenuItem('Coffee', 3)
menu_item4 = MenuItem('Orange Juice', 2)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]


index = 0

for menu_item in menu_items:
    # Print out in the format '0. Sandwich: $5' for each index
    print(str(index)+". "+menu_item.info())
    index+=1
    
    
