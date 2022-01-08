from time import sleep
import random
import datetime

#Var init for stages
printing = False
vari = False
loops = False
checknum = 0

#Awaiting input function

#Save file function 

#Introduction, input name and check
def intro():
    print("Welcome to Marwan's CIL Python Tutorial.")
    sleep(2)
    pname = input("To start, Please input your name: ")

    name_choice = input("Hello " + pname + ", is that correct?")

    while (name_choice != "Yes"):
        pname = input("Please input your name again: ")
        name_choice = input("Hello " + pname + "is that correct?")


    print("Well " + pname + ", nice to meet you, we will first start with the basics in Python or any programming language that is.")
    sleep(4)
    print("Printing!")
    sleep(2)


#First stage, printing
def printing_stage():
    while printing == False:
        print("In Python, we use the print() function to display stuff on the user's screen. For example, print('Hello World') will display Hello World on your screen. Try it!")

    first_print = input()
    try:
        exec(first_print)
        exec("checknum = 1")
    except:
        pass

    if checknum == 0:
        print("There was an error with your statement. Try again. (Hint: It probably has something to do with your quotation marks or brackets)")
        sleep(5)
    elif first_print == 'print("Hello World")' or first_print == "print('Hello World')":
        printing == True
    else:
        print("I see you printed something else... it's fine, you do you.")
        printing == True


#Second stage, variables
def vari_stage():
    while vari == False:
        
        def variable_tutorial():
            print("To initialize a variable, in python we just use this command: (variable_name = (contents of variable))")
            sleep(4)
            print("This might be a bit confusing at first but an example should help, age = 16")
            sleep(4)
            print("As we can see now the variable, which is basically a box holding a number in this case, holds the number 16 and we can call back on this whenever we want.")
            sleep(4)
            print("Try it yourself! Make a variable.")
            first_vari = input()
            try:
                exec(first_vari)
                vari = True
                return first_vari
            
            except:
                reminder = input("Something is wrong with your code. Would you like to be reminded of how to intialize a variable? If so press Y, otherwise press any other button to try again.")
                if reminder == "Y":
                    variable_tutorial()
                else:
                    execute_var()
        def execute_var():
            print("Make a variable.")
            first_vari = input()
            try:
                exec(first_vari)
            except:
                reminder = input("Something is wrong with your code. Would you like to be reminded of how to intialize a variable? If so press Y, otherwise press any other button to try again.")
                while reminder != "Y":
                    execute_var()
            
        print("Another important concept that is to be learnt in Python is handling variables.")
        sleep(4)
        variable_tutorial()
        print("Great job! Now we can try and use the print() function we learnt earlier, to print this variable you just made! Just call back the variable inside the print function. I'll let you figure this one out on your own (;")
        print_vari = input()
        try:
            exec(print_vari)
        except:
            print_reminder = input("Uh Oh, something went wrong with your code. Would you like a hint?")

#printing_stage()
#save_choice = input("Would you like to continue or save? C for continue or any other button to save and stop.")   
#if save_choice != "C":
#    pass  #save function to be added here
#else:
#    pass

vari_stage()
