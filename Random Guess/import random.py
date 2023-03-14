import random
target= random.randint(1,100)
print(target)
trying = "You tried %s times to solve it"
start = input('''Do you Wanna Start the Game ? (Input "y" to Start or "n" to Finish the Game)  ''')
if start == "y" :
    guessnumber= int(input("Guess it From 1 to 100 (Note, Any time For Exit the game , insert 0): "))
    i = 1
    while (target != guessnumber and guessnumber !=0) :
        if guessnumber >=0 and guessnumber <= 100 : # If the entered number is within the correct range
            if guessnumber < target :
                print(" Low ")
            else  :
                print(" High ")
            if abs(guessnumber-target) <= abs(3): # این تابع قدر مطلق هست ، حاصل منفی را مثبت میکند
                print("So close :)") # Idea From Mr.Daniyal Ghasemi
            if i % 3 == 0 : # Idea From Dear Reyhaneh Ramezani
                stop = input('''Do you Wanna Show the Target and Stop the Game? (Input "y" to Show or "n" to Continue)  ''')
                if stop == "y" :
                    print(target)
                    break
        else :
            print("Your Guess is Out of Correct Range ")
        guessnumber= int(input("Guess it : ")) #For Input Number
        i+=1
    if guessnumber == target :
        print(" *** WON *** ")   
        print(trying % i)
        if i <= 3 :
                print("You Are Genius :)")
        else :
                print('''It's Okey''')    
    print("Thank you for playing!")    
else :
    print("Have a Good Day :(")