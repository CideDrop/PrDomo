
#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# Detect movement using a PIR module
#
# Author : CideDrop
# Date   : 31/05/2018

# Import required Python libraries
import RPi.GPIO as GPIO
import time


# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_PIR = 7

print "PIR Module Test (CTRL-C to exit)"

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo

Current_State  = 0
Previous_State = 0

try:

  print "Waiting for PIR to settle ..."

  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0

  print "  Ready"

  # Loop until users quits with CTRL-C
  while True :

    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)

    if Current_State==1 and Previous_State==0:
      # PIR is triggered
      print  time.strftime(" Motion detected : %Y-%m-%d %H:%M:%S")
      # LOG write LogPIR.txt
      f = open('LogsPIR.txt','a')
      f.write("\n"+ time.strftime(" Motion detected : %Y-%m-%d %H:%M:%S"))
      f.close()

      # Record previous state
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      print "  Ready"
      Previous_State=0

    # Wait for 10 milliseconds
    time.sleep(0.01)

except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()




