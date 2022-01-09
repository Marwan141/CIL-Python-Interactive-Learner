from time import sleep
import random
import datetime
import os

#Var init for stages
printing = False
vari = False
loops = False
print_retry = True
var_add = True
checknum = 0
finished_Test =  False
totalinput = ""
#Awaiting input function

#Save file function 

#Introduction, input name and check
def intro():
    print("Welcome to Marwan's CIL Python Tutorial.")
    sleep(2)
    pname = input("To start, Please input your name: ")

    name_choice = input("Hello " + pname + ", is that correct? ")

    while (name_choice != "Yes"):
        pname = input("Please input your name again: ")
        name_choice = input("Hello " + pname + ", is that correct? ")


    print("Well " + pname + ", nice to meet you, we will first start with the basics in Python or any programming language that is.")
    sleep(4)
    print("Printing!")
    sleep(2)


#First stage, printing
def printing_stage(printing, checknum):
    print("In Python, we use the print() function to display stuff on the user's screen. For example, print('Hello World') will display Hello World on your screen. Try it!")
    while printing == False:
        

        first_print = input()
        try:
            exec(first_print)
            checknum = 1
        except:
            pass

        if checknum == 0:
            print("There was an error with your statement. Try again. (Hint: It probably has something to do with your quotation marks or brackets)")
        elif first_print == 'print("Hello World")' or first_print == "print('Hello World')":
            printing = True
            sleep(4)

        else:
            print("I see you printed something else... it's fine, you do you.")
            printing = True
            sleep(4)


#Second stage, variables
def vari_stage():
    print("Good job!, another important concept that is to be learnt in Python is handling variables.")
    sleep(4)
    while vari == False:
        
        def variable_tutorial(print_retry, var_add):
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
            except:
                reminder = input("Something is wrong with your code. Would you like to be reminded of how to intialize a variable? If so press Y, otherwise press any other button to try again.")
                while reminder == "Y":
                    variable_tutorial()
                else:
                    print("Make a variable.")
                    first_vari = input()
                    try:
                        exec(first_vari)
                    except:
                        reminder = input("Something is wrong with your code. Would you like to be reminded of how to intialize a variable? If so press Y, otherwise press any other button to try again.")
                        
    
            #Part 2

            print("Great job! Now we can try and use the print() function we learnt earlier, to print this variable you just made! Just call back the variable inside the print function. I'll let you figure this one out on your own (;")
            while print_retry:
                print_vari = input() 
                try:
                    exec(first_vari + "\n" + print_vari)
                    print_retry = False
                except:
                    print_reminder = input("Uh Oh, something went wrong with your code. Would you like a hint?")
                    if print_reminder == "Y":
                        print("Just use the print function: print(your variable here), no need for quotation marks.")
                        sleep(1)
                    else:
                        pass
            print("We can do so much more with variables, like basic arithemetic if they are integers. Give it a try, create 2 variables with numbers down below, press enter after each line of code.")
            while var_add:
                var1 = input()
                var2 = input()
                print("Now add them up! Just do 'var1 + var2' but replace the 'var1' and 'var2' with the names of the variables you made. ")
                add_var = input()
                try:
                    exec(var1 + "\n" + var2 + "\n" + add_var)
                except:
                    remin_add = input("Something went wrong with your code! Would you like a reminder on how to add them up?")
                    if remin_add == "Y":
                        print("To add two variables up, just do 'var1 + var2' but replace the 'var1' and 'var2' with the names of the variables you made. ")
                        sleep(2)
                    else:
                        pass              
            print("We can also add strings which we call concatinating. I'll let you try that on your own time. I cba to code it.")

        variable_tutorial(True, True)

def first_test():
    print("Now to recap everything we have done, I want you to code a program in which you input the age of two people and find the mean of their ages. After this print it out. Once you're done type N and enter")
    print("Good luck!")
    while finished_Test == False:
        newline = input()
        if newline == "N" or newline == "n":
            try:
                exec(totalinput)
                finished_Test = True
            except:
                print("There was a problem with your code. Try again.")
        else:
            totalinput = totalinput + "\n" + newline 

intro()
printing_stage(False, 0)
vari_stage()




#printing_stage()
#save_choice = input("Would you like to continue or save? C for continue or any other button to save and stop.")   
#if save_choice != "C":
#    pass  #save function to be added here
#else:
#    pass

