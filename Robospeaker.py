import os

if __name__ == '__main__':
    print("Welcome to robospeaker !. Created by Harry")
    x=input("Enter what you want to speak ")
    # command= print(x)
    cmd= f"echo{x}"
    os.system(cmd)

