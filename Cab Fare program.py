#This is code for the Taxi Program.
print("Welcome to the Taxi Program.")
print()
print("This program will calculate how much a cab fare cost depending on the distance.")
print()
Distance=12
Total_Distance_Traveled=float(input("How many miles did you traveled?:"))
print()
if Total_Distance_Traveled<=Distance:
    Mile_Cost=2
    Total_Mile_Cost=(Total_Distance_Traveled)*(Mile_Cost)
    print("The cost of each mile will be $2.00 a mile.")
    print()
    print(f'Total amount due is ${Total_Mile_Cost:.2f}.')
if Total_Distance_Traveled>Distance:
    Mile_Cost=1.50
    Total_Mile_Cost=(Total_Distance_Traveled)*(Mile_Cost)
    print("The cost of each mile will be $1.50 a mile.")
    print()
    print(f'Total amount due is ${Total_Mile_Cost:.2f}.')
