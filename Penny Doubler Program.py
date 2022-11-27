#A code that will calculate how much you $$$ can make if you work a certain number of days. And get paid in cents.
print("Welcome to the Penny Calculator program.")
print()
print("This program will determine how much you would")
print()
print("make if you were to get paid cents per day.")
print()

Pay=float(input("Please enter how many cents you're being paid: "))
print()
Day=int(input("Please enter the number of days you're going to be working:"))
print()
print('Day\tPay Rate\tTotal Amount')
print("-------------------------------------")

Total = 0
Doubler = 2
Profit_Goal = 5000
for Day in range(1, Day):
    Total_Amount = (Pay * (Doubler ** Day)) - 0.01
    Total += Total_Amount
    Day_Payment = Pay * (Doubler ** (Day-1))
    print(f'{Day}\t{Day_Payment:6}\t{Total_Amount:16.2f}')

if Total_Amount > Profit_Goal:
    print(f'It is worth earning pay at this rate if you work for at least {Day} days because you just made ${Total_Amount:.2f}.')
    
