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
    sound = mixer.Sound("Mice On Venus.wav")
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
    input = ""
    while input != "E":
        input = input("\nWhat song do you want to play?")
        if Rick == False:
            sound.stop()
            if input == 1:
                sound = mixer.Sound("C418 - Blocks (Minecraft Volume Beta).wav")
            elif input == 2:
                sound = mixer.Sound("C418 - Stal (Minecraft Volume Beta).wav")
            elif input == 3:
                sound = mixer.Sound("C418 - Strad (Minecraft Volume Beta).wav")
            elif input == 4:
                sound = mixer.Sound("Cat.wav")
            elif input == 5:
                sound = mixer.Sound("Chirp.wav")
            elif input == 6:
                sound = mixer.Sound("Pigstep.wav")
            elif input == 7:
                sound = mixer.Sound("Mellohi.wav")
            elif input == 8:
                sound = mixer.Sound("Mice On Venus.wav")
            elif input == 9:
                Rick == True
            elif input == "S":
                sound.stop()
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
            input = input("\nWhat song do you want to play?")

        print("""Pick an option! (1-8, S, E)
             1. Blocks
             2. Stal
             3. Strad
             4. Cat
             5. Chirp
             6. Pigstep
             7. Mellohi
             8. Mice on Venus
             S. Stop
             E. Exit""")
        input = input("\n")
    sound.play()
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