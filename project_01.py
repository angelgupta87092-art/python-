menu={
    "pizza":35,
    "pastry":40,
    "momo":30,
    "chowmin":50,
    "chicken chilli":70,
    "egg roll":40
}

print("welcome to my restuarant")
print("menu")
print("pizza:Rs35\npastry:Rs40\nmomo:Rs30\nchowmin:Rs50\nchicken chilli:Rs70\negg roll:RS 70")

order_total=0
item_1=input("Enter your order=")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item {item_1}has been added to your order")
else:
    print("This item is currently not available")

another_order =input("do you want another order (yes/no)")
if another_order=="yes":
    item_2=input("Enter the name of second order ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"your item {item_2}has been added to your order")
    else:
        print("oder is not available yet")
print(f"You have to pay total amount{order_total}")






