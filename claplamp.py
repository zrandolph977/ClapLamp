import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def button_callback(channel): #Function called when button press is inputted.
    print("Button was pushed!")
    relayChannel = 12
    GPIO.setup(relayChannel, GPIO.OUT)
  

    if GPIO.input(relayChannel) == GPIO.LOW:
        GPIO.output(relayChannel, GPIO.HIGH)
    else:
       GPIO.output(relayChannel, GPIO.LOW)

buttonChannel = 8
#GPIO SETUP
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonChannel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(buttonChannel,GPIO.FALLING,callback=button_callback) # Setup event on pin 10 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
    






    


