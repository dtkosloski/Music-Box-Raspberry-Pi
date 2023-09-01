import time
import RPi.GPIO as GPIO
from pygame import mixer #for playing audio
import random

def setup(led1,led2,led3,button):
    """Used to setup all the leds and the button"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led1,GPIO.OUT)
    GPIO.setup(led2,GPIO.OUT)
    GPIO.setup(led3,GPIO.OUT)
    GPIO.setup(button,GPIO.IN)

def play(prevState,currentState,sound,led1,led2,led3):
    """Plays the leds and the sound"""
    #run this code if I was previously pressing button and have now let go
    if currentState == False and prevState == True:
        if mixer.get_busy() == False: #only plays if it isnt already playing
            GPIO.output(led2, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(led2, GPIO.LOW)
            
            GPIO.output(led1, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(led1, GPIO.LOW)
            
            GPIO.output(led3, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(led3, GPIO.LOW)
            
            GPIO.output(led2, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(led2, GPIO.LOW)
            
            GPIO.output(led1, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(led1, GPIO.LOW)
            
            GPIO.output(led3, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(led3, GPIO.LOW)

            sound.play()
        else:
            sound.stop()
            
    return currentState # current state will become the prevState

def main():
    led1 = 17
    led2 = 27
    led3 = 22
    button = 21
    setup(led1,led2,led3,button)
    mixer.init()#initializes the audio mixer (via the constructor)
    try:
        prevState = True
        while True:
            num = random.randint(1,4)
            if num == 1:
                sound = mixer.Sound("gryffindor.wav")
            elif num == 2:
                sound = mixer.Sound("hufflepuff.wav")
            elif num == 3:
                sound = mixer.Sound("ravenclaw.wav")
            elif num == 4:
                sound = mixer.Sound("slytherin.wav")
            currentState = GPIO.input(button)
            prevState = play(prevState,currentState,sound,led1,led2,led3)
        
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
    
main()
