from microbit import *
import radio

'''
CONTROLLER CODE
'''

index = 0
minIndex = 0
maxIndex = 0
# List holding connected devices
devices = []

triggerMessage = "trigger_"

def sendMessage(message, device):
    # Send a message to the selected microbit
    radio.send(message + device)
    display.show(Image.HAPPY)
    sleep(2000)

def getConnectedDevices(message):
    # Get message
    # If message is "hey, set me up", add it into the list
    if message.startswith("stpreq"):
        deviceNumber = message.split("_")[1]
        devices.append(deviceNumber)
        display.scroll(deviceNumber + " added", wait=False)
        radio.send("stpack_" + deviceNumber)


radio.config(group=23)
radio.on()
while True:
    message = radio.receive()
    if message:
        getConnectedDevices(message)
    deviceCount = len(devices)
    if deviceCount > 0:
        maxIndex = deviceCount - 1
        if button_a.is_pressed() and button_b.is_pressed():
            # Send the message
            sendMessage(triggerMessage, devices[index])
        if button_b.was_pressed() and index < maxIndex:
            # Move right in the device list
            index += 1
            display.show(devices[index])
        elif button_a.was_pressed() and index > minIndex:
            # Move left in the device list
            index -= 1
            display.show(devices[index])


