#This program will calculate the total price of items when doing food shopping.
print("Welcome To The Super Market Program.")
print()
print("This program will calculate total price of your three items.")
print()
Item_One=int(input("Pass The First Item Quantity:"))
print()
Item_Two=int(input("Pass The Second Item Quantity:"))
print()
Item_Three=int(input("Pass The Third Item Quantity:"))
print()
Price_One=float(input("Pass The First Item's Price:"))
print()
Price_Two=float(input("Pass The Second Item's Price:"))
print()
Price_Three=float(input("Pass The Third Item's Price:"))
print()
Tax_Rate=float(input("What is the Tax rate?:"))
Tax_Decimal=Tax_Rate/100
Total_Price_One=(Item_One)*(Price_One)
Total_Price_Two=(Item_Two)*(Price_Two)
Total_Price_Three=(Item_Three)*(Price_Three)
Sub_Total=Total_Price_One + Total_Price_Two + Total_Price_Three
Total_Sales_Tax_Amount=(Sub_Total)*(Tax_Decimal)
Final_Price=(Total_Sales_Tax_Amount)+(Sub_Total)
print(f'Your subtotal is ${Sub_Total}.')
print()
print(f'Your sales tax amount is ${Total_Sales_Tax_Amount:.2f}.')
print()
print(f'Total amount due is ${Final_Price:.2f}.')
