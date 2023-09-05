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
             1. Song #1
             2. Song #2
             3. Song #3
             4. Song #4
             5. Song #5
             6. Song #6
             7. Song #7"""
    )
    
    input = ("\nWhat song do you want to play?")
    if Rick == True:
        if input == 1:
            sound = mixer.Sound("Mice On Venus.wav")
        elif input == 2:
            sound = mixer.Sound("Mice On Venus.wav")
        elif input == 3:
            sound = mixer.Sound("Mice On Venus.wav")
        elif input == 4:
            sound = mixer.Sound("Mice On Venus.wav")
        elif input == 5:
            sound = mixer.Sound("Mice On Venus.wav")
        elif input == 6:
            sound = mixer.Sound("Mice On Venus.wav")
        elif input == 7:
            sound = mixer.Sound("Mice On Venus.wav")

    else:
        sound = mixer.Sound("RickRoll.wav")
    print("Press ctrl+c to stop")
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