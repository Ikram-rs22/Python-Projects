import random


z = "y"

while(z == "y"):
    x = random.randint(1, 6)
    if(x==1):
        print("----------")
        print("|        |")
        print("|    0   |")
        print("|        |")
        print("----------")
    elif(x==2):
        print("----------")
        print("|        |")
        print("|   00   |")
        print("|        |")
        print("----------")
    elif(x==3):
        print("----------")
        print("|        |")
        print("|   000  |")
        print("|        |")
        print("----------")
    elif(x==4):
        print("----------")
        print("|        |")
        print("|   0 0  |")
        print("|   0 0  |")
        print("----------")
    elif(x == 5):
        print("----------")
        print("|        |")
        print("| 0  0 0 |")
        print("|   00  |")
        print("----------")
    else:
        print("----------")
        print("|        |")
        print("|   000  |")
        print("|   000  |")
        print("----------")

    z = input("y or n : ")