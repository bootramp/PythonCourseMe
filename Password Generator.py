import random
print("Wellcome To Password Generator\n")
leng = int(input("How many Character Do you need ? (Recomendation : 4 to 6 is week , 6 to 12 good , 12 to 22 is strong) -> "))
result = []
symbol = input("Do you need Symbol ? (y/n)  ")
number = input("Do you need Number ? (y/n)  ")
normal = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]
up = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z"]
char = ["!" , "@" , "#" , "$" , "%" , "^" , "&" , "*" , "(" , ")" , "-" , "/" , "?" , ">" , "<" , "~"]
num = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]
normal.extend(up)
def calculator():
    for i in range(0,leng):
        result.extend(random.choice(normal))
# if Symbol want
if symbol == "y" :
    normal.extend(char)
    # if number want
    if number == "y" :
        normal.extend(num)
        calculator()
    # if number not need
    else :
        calculator()
# if Symbol not need
else :
    # if number want
    if number == "y" :
        normal.extend(num)
        calculator()
    # if number not need
    else :
        calculator()
print("Result : " + ''.join(result))
