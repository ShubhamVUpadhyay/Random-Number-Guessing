#Write  a program to demonstrate number guessing game
import random
while True:
    userchoice=int(input('''Play number Guessing ?
1 Yes Continue
2 No
'''))
    if userchoice==1:
                   user_num=int(input("Enter a number : "))
                   system_num=random.randint(1,101)
                   print("Your number is :",user_num)
                   print("Computer number is : ",system_num)
                   if user_num==system_num:
                       print("Woah You have guessed the correct number")
                   elif user_num>system_num:
                       print("Guessed number is greater than actual number")
                   else:
                       print("Guessed number is smaller than actual number")
                   print("\n \n**************************************************** \n \n")
     
    else:
        print("You have been exited")
        break

