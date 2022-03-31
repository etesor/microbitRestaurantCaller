from microbit import *
import radio

'''
RECEIVER CODE
'''
# Change this id in every new microbit
deviceId = "1"

setMeUpMessage = "stpreq_"
triggerMessageStart = "trigger"

def triggerAction(deviceId):
    while not button_a.was_pressed():
        display.show(Image.ANGRY)
    display.clear()
    display.show(deviceId)

radio.config(group=23)
radio.on()
setup = False
while True:
    message = radio.receive()
    if setup is False:
        radio.send(setMeUpMessage + deviceId)
        while setup is False:
            message = radio.receive()
            if message:
                if message.startswith("stpack") and message.endswith(deviceId):
                    display.show(message.split("_")[1])
                    setup = True
    if message and message.startswith(triggerMessageStart) and message.endswith(deviceId):
        triggerAction(deviceId)
