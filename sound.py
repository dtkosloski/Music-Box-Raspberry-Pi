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
        print("Press ctrl+c to stop")
        exit()
    
main()