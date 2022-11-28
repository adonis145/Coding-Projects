#Code for determining enrollment eligibility for the School of Zicklin (my alma mater).
print("welcome to the enrollment program.")
print()
print("This program will determine your elgibility in joining the school of Zicklin.")
print()
Com_1010=str(input('Have you completed COM 1010? Y/N:'))
if Com_1010=="N" or Com_1010=="n":
    print("You don't meet the requirements to enter Zicklin. Sorry.")
    exit(Com_1010=="N" or Com_1010=="n")
    
else:
    Com_1010==("Y") or Com_1010==("y")
    print("Great! Next Question.")

Eng_2150=str(input('Have you completed ENG 2150? Y/N:'))

if Eng_2150=="N" or Eng_2150=="n":
    print("You don't meet the requirements to enter Zicklin. Sorry.")
    exit(Eng_2150=="N" or Eng_2150=="n")
else:
    Eng_2150=="Y" or Eng_2150=="y"
    print("Great! You satisfied the communication requirements!")
    print()
    print("Let's check some additional requirements...")
    print()
    print("""Use the following table to enter your numeric grades for each course:
A=4
A-=3.7
B+=3.3
B=3.0
B-=2.7
C+=2.3
C=2.0
C-=1.7
D+=1.3
D=1.0
F=0.0""")
print()

Minimum_Gpa=2.25
Minimum_Credits=45
Acc_201=float(input('Your grade in ACC 2101? : '))
print("Great! Next question.")

Cis_220=float(input('Your grade in CIS 2200? :'))
print("Great! Next question.")

Eco_100=float(input("Your grade in ECO 1001?: "))
print("Great! Next question.")

Eco_1002=float(input("Your grade in ECO 1002?: "))
print("Great! Next question.")
    
Eng_2100=float(input("Your grade in ENG 2100?: "))
print("Great! Next question.")
    
Law_1101=float(input("Your grade in Law 1101?: "))
print("Great! Next question.")

Calculus=float(input("Your grade in one of the calculus courses? :"))
print("Great! Next question.")

STA_2000=float(input("Your grade in STA 2000?: "))

GPA_Average=((Acc_201+Cis_220+Eco_100+Eco_1002+Eng_2100+Law_1101+Calculus+STA_2000)/8)
if GPA_Average<Minimum_Gpa:
    print("Sorry. You don't meet the requirements.")
    exit(((Acc_201+Cis_220+Eco_100+Eco_1002+Eng_2100+Law_1101+Calculus+STA_2000)/8))
else:
    print(f'That was hard work! Your pre-business GPA is: {GPA_Average:.2f}')

Total_Credits=float(input("How many credits completed?:"))
if Total_Credits<Minimum_Credits:
    print("Sorry. You need at least 45 credits to be eligible.")
    exit(Total_Credits<Minimum_Credits)
else:
    print("Excellent. So far so good! Just one last question.")

Total_Baruch_GPA=(float(input("What is your overall Baruch GPA?:")))
if Total_Baruch_GPA<Minimum_Gpa:
    print("Sorry, you need at least an overall Baruch GPA of 2.25 or higher to be accepted.")
    exit(Total_Baruch_GPA<Minimum_Gpa)
else:
    print("Congratulations. Welcome to the Zicklin School of business!")
