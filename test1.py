finished_Test = False
totalinput = ""
while finished_Test == False:
    newline = input()
    if newline == "N" or newline == "n":
        finished_Test = True
    else:
        totalinput = totalinput + "\n" + newline 
    
try:
    exec(totalinput)
except:
    print("There was a problem with your code. Try again.")