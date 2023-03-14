import random
coin = "line" , "lion"
#target = random.choice(coin)
def flipp():
    guessnumber = input("Line or Lion ---> ")
    i = 0
    wrong_counter = 0
    while (guessnumber != '0'):
        target = random.choice(coin)
        if guessnumber == "lion" or guessnumber == "line" :
            print(target)
            if guessnumber == target :
                i+=1
                if i % 3 == 0 :
                    print("Awesome")
            else :
                i = 0
        else :
            print("Wrong Input")
            print(target)
            i = 0
            wrong_counter+=1
        if wrong_counter == 3 :
            print("Your number of mistakes has exceeded the limit")
            break
        guessnumber = input("Line or Lion ---> ")
start = input("Do you Wanna Play the Game ? press 'y' for yes or press 'n' for no --->  ")
if start == 'y' or start == 'Y' or start == 'yes' :
    print("Welcome To Flip a coin Game")
    flipp()
else :
    print("Have a Good Day :( ")
print("Good Luck")