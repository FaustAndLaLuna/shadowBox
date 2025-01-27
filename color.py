import board
import math
import neopixel
import time
import sys

maxPixels = 12
pixelsPin = board.D18
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixelsPin, maxPixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

back = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
mid = [24,25,26,27,28,29,30,31,32,33,34,35]
front = [36,37,38,39,40,41,42,43,44,45,46,47]

left = [0,1,2,3,20,21,22,23,24,25,26,27,44,45,46,47]
middle = [4,5,6,7,16,17,18,19,28,29,30,31,40,41,42,43]
right = [8,9,10,11,12,13,14,15,32,33,34,35,36,37,38,39]

top = [0,1,10,11,12,13,22,23,24,25,34,35,36,37,46,47]
center = [2,3,8,9,14,15,20,21,26,27,32,33,38,39,44,45]
bot = [4,5,6,7,16,17,18,19,28,29,30,31,40,41,42,43]



#########################################################
#########################################################
#########################################################
#########################################################
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)
 
def applyToAll(color):
    for section in sections:
        for pixNum in section:
            pixels[pixNum] = color

def applyToSection(section, color):
	for pixNum in section:
		pixels[pixNum] = color
 
def transitionAllToColor(startColor, endColor, totalTime):
    rDelta = (endColor[0] - startColor[0]) / (totalTime/50)
    gDelta = (endColor[1] - startColor[1]) / (totalTime/50)
    bDelta = (endColor[2] - startColor[2]) / (totalTime/50)
    rStarting = startColor[0]
    gStarting = startColor[1]
    bStarting = startColor[2]

    for i in range(0, int(totalTime/50)):
        applyToAll((int(rStarting + rDelta * i),int(gStarting + gDelta * i),int(bStarting + bDelta * i)))
        # applyToAll((int(color[0]), int(color[1]), int(color[2])))
        pixels.show()
        time.sleep(.045)

def transitionSectionsToColor(startColor0, endColor0, startColor1, endColor1, startColor2, endColor2, totalTime):
    rDelta0 = (endColor0[0] - startColor0[0]) / (totalTime/50)
    gDelta0 = (endColor0[1] - startColor0[1]) / (totalTime/50)
    bDelta0 = (endColor0[2] - startColor0[2]) / (totalTime/50)
    rDelta1 = (endColor1[0] - startColor1[0]) / (totalTime/50)
    gDelta1 = (endColor1[1] - startColor1[1]) / (totalTime/50)
    bDelta1 = (endColor1[2] - startColor1[2]) / (totalTime/50)
    rDelta2 = (endColor2[0] - startColor2[0]) / (totalTime/50)
    gDelta2 = (endColor2[1] - startColor2[1]) / (totalTime/50)
    bDelta2 = (endColor2[2] - startColor2[2]) / (totalTime/50)

    rStarting0 = startColor0[0]
    gStarting0 = startColor0[1]
    bStarting0 = startColor0[2]
    rStarting1 = startColor1[0]
    gStarting1 = startColor1[1]
    bStarting1 = startColor1[2]
    rStarting2 = startColor2[0]
    gStarting2 = startColor2[1]
    bStarting2 = startColor2[2]

    for i in range(0, totalTime//50):
        applyToSection(section1, (int(rStarting0 + rDelta0 * i),int(gStarting0 + gDelta0 * i),int(bStarting0 + bDelta0 * i)))
        applyToSection(section2, (int(rStarting1 + rDelta1 * i),int(gStarting1 + gDelta1 * i),int(bStarting1 + bDelta1 * i)))
        applyToSection(section3, (int(rStarting2 + rDelta2 * i),int(gStarting2 + gDelta2 * i),int(bStarting2 + bDelta2 * i)))
        pixels.show()
        time.sleep(.045)
############################################################################
############################################################################
############################################################################
############################################################################
def rainbowCycle(wait):
    for j in range(255):
        for i in range(3):
            pixel_index = (i * 256 // 3) + j
            applyToSection(sections[i], wheel(pixel_index&255))
        pixels.show()
        time.sleep(wait)

def rainbowCycleAll(wait):
    for j in range(255):
        applyToAll(wheel(j))
        pixels.show()
        time.sleep(wait)

def pingpongAll(startingColor, endColor, halftime):
    transitionAllToColor(startingColor, endColor, halftime)
    transitionAllToColor(endColor, startingColor, halftime)

def pingpongSections(sColor1, eColor1, sColor2, eColor2, sColor3, eColor3, halftime):
    print(halftime)
    milliseconds = int( time.time() * 1000 )
    transitionSectionsToColor(sColor1,eColor1,sColor2,eColor2,sColor3,eColor3,halftime)
    transitionSectionsToColor(eColor1,sColor1,eColor2,sColor2,eColor3,sColor3,halftime)
    milliseconds -= int( time.time() * 1000 )
    print(milliseconds)

def colorAll(color):
    pixels.fill(color)
    pixels.show()

def colorSections(color1, color2, color3):
    applyToSection(section1, color1)
    applyToSection(section2, color2)
    applyToSection(section3, color3)
    pixels.show()

def blink():
    turnOff = (0,0,0)
    for i in range(0,4):
        colorAll([255,255,255])
        time.sleep(0.3)
        colorSections(turnOff, turnOff, turnOff)
        time.sleep(0.4)
############################################################################
############################################################################
############################################################################
############################################################################
brightness = float(sys.argv[1])
sectionsArg = sys.argv[2]
funName = sys.argv[3]

if sectionsArg == "backToFront":
    section1 = back
    section2 = mid
    section3 = front
elif sectionsArg == "leftToRight":
    section1 = left
    section2 = middle
    section3 = right
elif sectionsArg == "topToBottom":
    section1 = top
    section2 = center
    section3 = bot

sections = [section1, section2, section3]
toRemove = []
for i in range(0, 100):
    if i >= maxPixels:
        toRemove.append(i)
for i in toRemove:
    if i in section1:
        section1.remove(i)
    if i in section2:
        section2.remove(i)
    if i in section3:
        section3.remove(i)

if funName == "rainbowCycle":
    wait = float(sys.argv[4])
    while True:
        rainbowCycle(wait)

if funName == "rainbowCycleAll":
    wait = float(sys.argv[4])
    while True:
        rainbowCycleAll(wait)

if funName == "pingpongAll":
    startingColor = eval(sys.argv[4])
    endColor = eval(sys.argv[5])
    halftime = int(sys.argv[6])//2
    while True:
        pingpongAll(startingColor, endColor, halftime)

if funName == 'pingpongSections':
    sColor1 = eval(sys.argv[4])
    sColor2 = eval(sys.argv[5])
    sColor3 = eval(sys.argv[6])
    eColor1 = eval(sys.argv[7])
    eColor2 = eval(sys.argv[8])
    eColor3 = eval(sys.argv[9])
    halftime = int(sys.argv[10])//2
    while True:
        pingpongSections(sColor1, eColor1, sColor2, eColor2, sColor3, eColor3, halftime)

if funName == 'colorAll':
    color = eval(sys.argv[4])
    colorAll(color)
    while True:
        time.sleep(10)

if funName == 'color':
    color1 = eval(sys.argv[4])
    color2 = eval(sys.argv[5])
    color3 = eval(sys.argv[6])
    colorSections(color1, color2, color3)
    while True:
        time.sleep(10)

if funName == 'turnOff':
    test = (0,0,0)
    colorSections(test, test, test)

if funName == 'blink':
    blink()