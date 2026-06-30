import pyfiglet

price = 0
purchases = 0
discount = 0

text_art = pyfiglet.figlet_format("Magico Apps\nDiscount calculator")
print(text_art)


purchases = float(input("Enter the purchase amount: "))

if purchases < 100:
    discount = 0
    price = purchases
elif purchases > 100 and purchases < 500:
    discount = 10
    price = (purchases * 90 / 100)
elif purchases >= 500:
    discount = 20
    price = (purchases * 80 / 100)


print(f"The discount amount available to you is: {discount}%")
print(f"Total amount required after discount: {price}$")
