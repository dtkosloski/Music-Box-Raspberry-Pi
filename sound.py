import time
import RPi.GPIO as GPIO
from pygame import mixer #for playing audio

def play(prevState,currentState,sound):
    #run this code if I was previously pressing button and have now let go
    if currentState == False and prevState == True:
        if mixer.get_busy() == False: #only plays if it isnt already playing
            sound.play()
        else:
            sound.stop()
            
    return currentState # current state will become the prevState

def main():
    mixer.init()#initializes the audio mixer (via the constructor)
   
    Rick = False
    print("""Pick a song! (1-8)
             1. Blocks
             2. Stal
             3. Strad
             4. Cat
             5. Chirp
             6. Pigstep
             7. Mellohi
             8. Mice on Venus"""
    )
    choice = 11
    while choice != 0:
        sound = mixer.Sound("Mice On Venus.wav")
        choice = int(input("\nWhat song do you want to play? "))
        if Rick == False:
            sound.stop()
            if choice == 1:
                sound = mixer.Sound("C418 - Blocks (Minecraft Volume Beta).wav")
            elif choice == 2:
                sound = mixer.Sound("C418 - Stal (Minecraft Volume Beta).wav")
            elif choice == 3:
                sound = mixer.Sound("C418 - Strad (Minecraft Volume Beta).wav")
            elif choice == 4:
                sound = mixer.Sound("Cat.wav")
            elif choice == 5:
                sound = mixer.Sound("Chirp.wav")
            elif choice == 6:
                sound = mixer.Sound("Pigstep.wav")
            elif choice == 7:
                sound = mixer.Sound("Mellohi.wav")
            elif choice == 8:
                sound = mixer.Sound("Mice On Venus.wav")
            elif choice == 10:
                Rick == True
            elif choice == 9:
                mixer.stop()
            if choice != 9:
                sound.play()
        else:
            sound = mixer.Sound("Rick Astley - Never Gonna Give You Up (Official Music Video).wav")
            print("""Pick a song! (1-8)
             1. Blocks
             2. Stal
             3. Strad
             4. Cat
             5. Chirp
             6. Pigstep
             7. Mellohi
             8. Mice on Venus""")
            choice = int(input("\nWhat song do you want to play? "))

        print("""Pick an option! (0-9)
             1. Blocks
             2. Stal
             3. Strad
             4. Cat
             5. Chirp
             6. Pigstep
             7. Mellohi
             8. Mice on Venus
             9. Stop
             0. Exit""")
        
    exit()
    try:
        prevState = True
        while True:
            currentState = True
            prevState =  True
            play(prevState,currentState,sound)
        
    except KeyboardInterrupt:
        GPIO.cleanup()
        sound.play()
        
        exit()
    
main()