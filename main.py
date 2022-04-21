from pickletools import pyset
from re import ASCII
import serial, requests

# Discord Webhook URL in CPE Design Project server.
webhookurl = "https://discord.com/api/webhooks/966689045210099712/lwymg23yagGEykl2O4ZAfp8v4vMpfnec2Y_ntlW7Bj90-7CsGfAOvBENL3kowx1wvZ02"
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

var = 0
sent = False

while True:
    
    value = arduino.readline().decode("ASCII")

    if value == "1":
        if sent == False:
            var+=1
            response = requests.post(url=webhookurl, 
            json={"content":"This is Arduino {}. \n @everyone".format(var)})
            sent = True  

    if value == "0":
        sent = False

