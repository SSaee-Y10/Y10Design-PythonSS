# Here is a program to show how to use "if - elif - else"
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Mr. Jugoon
# Upper Canada College

# Put down some options for the user to choose from...


print("1. orange juice  ")
print("2. water ")
print("3. ice tea ")
print("4. milk ")
print("5. chocolate milk ")
print("Choose one of the options above")
 
choise = int(input("please make a selction \n"))
NumItems = int(input("please specify how many items you would like \n"))
money = float(input("please enter how much money you have with no $ sign... \n")) # "money" is a float data-type because it is a decimal

if choise == 1:
    print(" 2.30$ ")
elif choise == 2:
    print (" 2.00$ ")
elif choise == 3:
    print (" 3.50$ ")
elif choise == 4:
    print (" 2.25$ ")
elif choise == 5:
    print ("  3.00 ")
else:
    print ("This is not a valid choise")
    print ("Hope you have a great day anyway!")

print ("You have chosen to buy " + str(NumItems) + " items")

if choise == 1: money = money - (NumItems * 2.30)
if choise == 2: money = money - (NumItems * 2.00)
if choise == 3: money = money - (NumItems * 3.50)
if choise == 4: money = money - (NumItems * 2.25)
if choise == 5: money = money - (NumItems * 3.00)

print ("You now have  " + str(money) + " dollars left")


# This is a way to gracefuuly exit the program
input("Thanks for your parchase!")
