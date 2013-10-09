import RPi.GPIO as GPIO
import time
import requests

SLEEP_TIME=60
RED_LED=22
GREEN_LED=17

current_status="Off"

# Use logical pin numbers
GPIO.setmode(GPIO.BCM)
# Set up header pins
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)

def showBuildStatus(buildStatus):
  print ("Status is '%s'" % (buildStatus))
  if buildStatus == "succeeded":
    # Set so just the green LED on
    GPIO.output(GREEN_LED, True)
    GPIO.output(RED_LED, False)
  elif buildStatus == "failed":
    # Set so just the red LED on
    GPIO.output(RED_LED, True)
    GPIO.output(GREEN_LED, False)
  else:
    # Set so all LED's are off
    GPIO.output(RED_LED, False)
    GPIO.output(GREEN_LED, False)

def getBuildStatus():
  status = "Unkown"

  # Look up the status in TFS
  r = requests.get('https://martin.visualstudio.com/DefaultCollection/_apis/build/Builds?definition=RadioTFS%20Producer%20Ap%20CI&$top=1', auth=('martinwo', 'InsertMyPasswordHere...')) 
  response = r.json()
  status = response['value'][0]['status']

  return status
    
try:

  print ("Start loop")
  
  while True:
    buildStatus = getBuildStatus()
    showBuildStatus(buildStatus)
    time.sleep(SLEEP_TIME)

except KeyboardInterrupt:
      GPIO.cleanup()

