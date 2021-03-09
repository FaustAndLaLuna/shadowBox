import requests, json, time, os

host = 'http://10.0.1.9:81'
colorCheckRoute = '/updateDaniBox'
contactRoute = '/edToDani'

lastIDColor = None
lastIDContact = None
changeString = "sudo pm2 start 'sudo python3 /home/fall/shadowBox/color.pyTEXTTOREPLACE' --name color"
currChange = "sudo pm2 start 'sudo python3 /home/fall/shadowBox/color.py 0.5 leftToRight rainbowCycle .0025' --name color"
stopProcess = "sudo pm2 delete color"
timesWaitedContact = 0

def applyColorResponse():
    global lastIDColor
    global currChange
    try:
        response = requests.get(url=host+colorCheckRoute)
        colorObj = response.json()
        currID = colorObj['currID']
        if currID != lastIDColor:
            lastIDColor = currID
            os.system(stopProcess)
            currChange = changeString.replace('TEXTTOREPLACE', colorObj['arguments'])
            os.system(currChange)
    except:
        print("El servidor no está respondiendo. Reintentando.")
        time.sleep(5)
        return

def blink():
    os.system(stopProcess)
    os.system("sudo pm2 start 'sudo python3 /home/fall/shadowBox/color.py 1.0 backToFront blink' --name color")
    os.system(stopProcess)
    time.sleep(3)
    os.system(currChange)


def applyContactResponse():
    global lastIDContact
    global timesWaitedContact
    try:
        response = requests.get(url=host+contactRoute)
        contactObj = response.json()
        currID = contactObj['currID']
        isActive = contactObj['isActive']
        timesWaitedContact %= 450
        if timesWaitedContact != 0:
            timesWaitedContact += 1
            return
        timesWaitedContact += 1
        if isActive:
            blink()
    except:
        print("El servidor no está respondiendo. Reintentando.")
        time.sleep(5)
        return

while True:
    for i in range(0, 5):
        time.sleep(.5)
        applyColorResponse()
    time.sleep(2)
    applyContactResponse()
