#Tax Code program. Allows you to calculate taxes. Based on Elizabeth Warren's Tax Proposal.
print("Welcome to the Tax program.")
print()
print("This program will calculate how much you owe to the government(oof).")
print()
Normal_Income=100000
High_Income=500000
Total_Income=float(input("Pass the total income:"))
if Total_Income<Normal_Income:
    Income_Tax=0.01
    Total_Tax_Due=(Total_Income)*(Income_Tax)
    print(f'You have earned ${Total_Income:,.2f} dollars last year.')
    print()
    print(f'You must pay a 1% income tax.')
    print()
    print(f'The tax of the current year is ${Total_Tax_Due:,.2f}.')
    
elif Total_Income>=High_Income:
    Income_Tax=0.05
    Cents_Owed=0.02
    Total_Tax_Due=(Total_Income)*(Income_Tax)
    Total_Amount_Owed=((Total_Income)-(High_Income))*(Cents_Owed)
    Total_Amount_Due=(Total_Tax_Due)+(Total_Amount_Owed)
    print(f'You have earned ${Total_Income:,.2f} dollars last year.')
    print()
    print(f'You must pay a 5% income tax.')
    print()
    print(f'And 2 cents for every dollar above $500,000.')
    print()
    print(f'The tax of the current year is ${Total_Amount_Due:,.2f}.')
else:
    Total_Income==Normal_Income
    Income_Tax=0.05
    Total_Taxed_Due=(Total_Income)*(Income_Tax)
    print(f'You have earned ${Total_Income:,.2f} dollars last year.')
    print()
    print(f'You must pay a 5% income tax.')
    print()
    print(f'The Tax of the current year is ${Total_Taxed_Due:,.2f}.')
