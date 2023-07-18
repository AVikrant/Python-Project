#water  -play water.mp3  3.5 litres -Done -  log
#Eyes -- Eyes.mp3  Eydone -log  30 mins
#Physical activity --physical.mp3  Pydone --log 45  mins


# pygame module for audio

from pygame import mixer
import datetime
import time

def get_time():
    current=datetime.datetime.now()
    t=current.strftime("%d/%m/%Y, %H:%M:%S")
    return t

def water():
    # time.sleep(1800)
    print(get_time(),"\nPlease drink water")
    # Instantiate mixer
    mixer.init()
    mixer.music.load('water.mp3.mp3')
    # Infinite loop
    while True:
        mixer.music.play()
        # take user input
        userInput = input("press drank ")
        if userInput != 'drank':
            print("Invalid entry")
            continue
        else:
            f = open("water.txt", "a")
            f.write("[" + str(get_time()) + "]-Water Drank\n")
            print(" log have been saved ")
            break
def eyes():
    # time.sleep(600)
    # start_time=time.ctime()
    while True:
        print(get_time(), "Please do Eyes exercise")
        mixer.init()
        mixer.music.load("eyes.mp3.mp3")
        mixer.music.play()
        userInput = input("")
        if userInput != 'Eydone':
            print("Invalid entry")
            continue
        else:
            f = open("eyes.txt", "a")
            f.write("[" + str(get_time()) + "]-Eyes exercise done\n")
            print(" log have been saved ")
            break
def physical_ex():
    # time.sleep(300)
    while True:
        print(get_time(), "Please do Physical exercise")
        mixer.init()
        mixer.music.load("physical.mp3.mp3")
        mixer.music.play()
        userInput = input("")
        if userInput != 'Pydone':
            print("Invalid entry")
            continue
        else:
            f = open("physical.txt", "a")
            f.write("[" + str(get_time()) + "]- Physical exercise done\n")
            print(" log have been saved ")
        break

if __name__ == '__main__':
    initial_water = time.time()
    initial_eyes = time.time()
    initial_physical = time.time()
    watersecs=5
    eyessecs=10
    physecs=20

    while (True):
        if time.time()-initial_water>watersecs:
            initial_water = time.time()
            water()
        if time.time()-initial_eyes>eyessecs:
            initial_eyes = time.time()
            eyes()
        elif time.time()-initial_physical>physecs:
            initial_physical = time.time()
            physical_ex()













