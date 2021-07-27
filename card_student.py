print("Please, enter the following information")

Firstname = input('First Name: ')
Lastname = input('Last Name: ')
Phonenumber = input('Phone Number: ')
JobTitle = input('Job Title: ')
Email = input('Email: ')
IDNumber = input('ID Number: ')

print()

print("Awesome! Now, if you want, enter with additional information")
user_colorhair = input('Your Hair Color :')
user_eyescolor = input('Your Eyes Color')
user_startmonth = input("Month that you will start")
user_training = input("Was you trainning?")

#Basic informations 
output = ("The Card is: ")
first  = (Lastname ,Firstname) 
Phone = (Phonenumber)
Job = (JobTitle)
email = (Email)
ID = (IDNumber)

#Addition Information
hair_color = (user_colorhair)
eye_color = (user_eyescolor)
datamonth = (user_startmonth)
trainingdecision = (user_training)

#Basic informations 
print(output)
print("----------------------------------------")
print(f"{Lastname.upper()}, {Firstname.capitalize()}")   
print(f"{Job.title()}")
print(f"ID: {IDNumber}")
print()
print(f"{email.lower()}")
print(f"{Phone}")
print("----------------------------------------")
print()
#Addition Information
print(hair_color)
print(eye_color)
print(datamonth)
print(trainingdecision)