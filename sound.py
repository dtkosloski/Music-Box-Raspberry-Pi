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
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21,GPIO.IN)
    mixer.init()#initializes the audio mixer (via the constructor)
    sound = mixer.Sound("microwave-oven-1.wav")
    
    try:
        prevState = True
        while True:
            currentState = GPIO.input(21)
            prevState = play(prevState,currentState,sound)
        
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
    
main()