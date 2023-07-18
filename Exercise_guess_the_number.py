# n=18
# take input from user
# user input is bigger or smaller
# # no guesses should be 5
# # print no of guesses
# Game over if guesses  finished
# No of guesses he took
# You won

n=18
count =1
while(count<=5):                                 #Number of Attempt should be till 5
    inp = int(input("\nPlease guess the number")) #Taking input from user
             #PRinting number attempts
                                  #increasing number of attempt by 1

#Using ifelse statements
    if inp<n:
        print("Ohho ! You entered smaller number")
    elif inp>n:
        print("Ohhoooo! You entered bigger number")
    else:
        print("Congratulation you guessed right number! YOU WON!\n")
        print(count,"No of guesses he took to finish")
        break
    print(5-count,"No of gusses left")
    print('Number of Attempt=', count)
    count = count + 1


else:
    print("Number of Attempt finished! GAME OVER")
