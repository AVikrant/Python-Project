# input s w g
# use while till 10
# Also count score

import random
i=0

while i < 10:

    i = i + 1
    win = 0
    lst = ["S", "W", "G"]
    score=[]
    Computer_choice = random.choice(lst)

    try:
        user_input = input("\nEnter your option: 1)S for Snake 2)W for Water 3)G for Gun\n")
        Your_input = user_input.upper()
        while Your_input!='S' or Your_input!='W' or Your_input!='G':
            print("wrong entry! input again")
            break
        if Your_input=="s" or Your_input=="S" or Your_input=="w" or Your_input=="W" or Your_input=="g" or Your_input=="G":
            print(f"Computer choose--{Computer_choice},You Choose--{Your_input}")


            if Your_input == Computer_choice:
                print("Match Draw")

            elif Your_input == "W" and Computer_choice == "S":
                print("You Lose")
            elif Your_input == "W" and Computer_choice == "G":
                    print("You win")
                    # win+=1
            elif Your_input == "G":
                if Computer_choice == "S":
                    print("You won")
                    win = win + 1
                    print(win)
                elif Computer_choice == "W":
                    print("You Lose")
            elif Your_input == "S":
                if Computer_choice == "G":
                    print("You Lose")
                elif Computer_choice == "W":
                    print("You win")
                    win = win + 1
                    print(win)
            print("Number of times played--", i)
            print("Attempt left",10-i)

        else:
            print("Invalid Entry")
            i=i-1
    except Exception as e:
        print(e)




