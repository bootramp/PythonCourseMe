from art import art
from replit import clear
import time
clear()
print(art)
Bidders = {}
print("********** Wellcome To Bidders Game **********")
Name = input("What is your name? ").lower()
Bid = int(input("Whats your Bid? $"))
Bidders[Name]=Bid
while True:
    Anyone = input("Are there any other bidders? Type 'yes' or 'no' ")
    if Anyone == "yes" or Anyone == "Yes" or Anyone == "y":
        clear()
        Name = input("What is your name? ").lower()
        Bid = int(input("Whats your Bid? $"))
        Bidders[Name]=Bid
    else :
        clear()
        max_key = max(Bidders, key=lambda k: Bidders[k])
        print(f"The Winner is {max_key} with a bid of ${Bidders[max_key]}")
        break

time.sleep(5)
clear()