#Author: Diogo Rangel Dos Santos
#Prove Milestone Week 04 and 03 Prove: Milestone - Meal Price Calculator

#childrensmealprince
childrenmeal = float(input("What is the price of a child's meal? $"))

# adultsmealprice
adultmeal = float(input("What is the price of adult's meal? $"))

#numbersbyhumanphase
howchildrens = int(input("How many children are there? "))
howadults = int(input("How many adults are there? "))

#tax
salestax = float(input("What is the sales tax rate? $"))

#totalbyclass
totalchildren = howchildrens * childrenmeal
totaladult = howadults * adultmeal

#subtotalcount and round
subtotal = round(totalchildren + totaladult, 2)
totalrate = round(subtotal * salestax / 100, 2)
total = round(subtotal + totalrate, 2)

#subtotalshow
print(f"The Subtotal of this account is: ${subtotal}")
print(f"Salex tax is: ${totalrate}")
print(f"The total is: ${total}")

#totalcalculation
amount = float(input("What is the payment amount? $"))
Change = round(amount - total, 2)
print(f"The change is: ${Change}")