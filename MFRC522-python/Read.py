import RPi.GPIO as GPIO
import MFRC522
import signal
import requests
import time
import json

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print("RFID Project")
print("Press Ctrl-C to stop.")

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print("Card detected")
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    if status == MIFAREReader.MI_OK:
        finalUid = ', '.join(str(i) for i in uid)
        finalUid = finalUid.replace(',','')
        finalUid = finalUid.replace(' ','')
        print(finalUid)
        reqAuth = requests.get('http://192.168.43.217:3030/v1/api/auth/find/'+finalUid)
        if reqAuth.status_code == 200:
            print('REQUEST UID : Success!')
            print(reqAuth.json())
            log = open("uid.txt","w")
            log = open("/var/www/html/Projet/MFRC522-python/uid.txt","w")
            log.write(finalUid)
            log.close()
        elif reqAuth.status_code == 404:
            print('REQUEST UID : Not Found.')
        time.sleep(1)
        #print reqAuth.content
        reqRasp =  requests.post("http://192.168.43.217:3030/v1/api/rfid", data={'raspberryUID':'RASP_DEMO_1','userKey':finalUid})
        print(reqRasp.status_code)
        if reqRasp.status_code == 201:
            print('REQUEST RASP : Success!')
        elif reqRasp.status_code == 404:
            print('REQUEST RASP : FAILED')
        #
        time.sleep(1)





