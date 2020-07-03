tickets = int(input("enter the no of tickets: "))
king=75
queen = 150
total_price = 0
refreshment=0
if tickets<5 or tickets>40:
    print("min of 5 or max 40 tickets can be booked at a time")
else:
    
    refr = input("do you want refreshment: ")
    if refr=="y":
        total_price+=tickets*50
    coupon = input("do you have coupon?:  ")
    circle = input("enter the circle: ")
    if circle=="k":
        total_price+= tickets*king
    elif circle=="q":
        total_price +=tickets*queen
    else:
        print("invlid input")
    
    if tickets>20 and coupon=="y":
        total_price -= total_price*0.12
        
    elif coupon=="y":
        total_price -= total_price*0.02
        
    elif tickets>20:
        total_price -= total_price*0.10
        

           
    print("total  price for ur tickets are: " ,total_price)
         

