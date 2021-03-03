import board
import math
import neopixel
import time

maxPixels = 40
pixelsPin = board.D18
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(pixelsPin, maxPixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

back = [0,1,2,3,4,5,6,7,8,9,10,11]
mid = [12,13,14,15,16,17,18,19,20,21,22,23]
front = [24,25,26,27,28,29,30,31,32,33,34,35]

left = [0,1,2,3,20,21,22,23,24,25,26,27]
middle = [4,5,6,7,16,17,18,19,28,29,30,31]
right = [8,9,10,11,12,13,14,15,32,33,34,35]

top = [0,1,10,11,12,13,22,23,24,25,34,35]
center = [2,3,8,9,14,15,20,21,26,27,32,33]
bot = [4,5,6,7,16,17,18,19,28,29,30,31]

toRemove = []
section1 = back
section2 = mid
section3 = front

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
sections = [section1, section2, section3]
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
    rDelta = int((endColor[0] - startColor[0]) / totalTime)
    gDelta = int((endColor[1] - startColor[1]) / totalTime)
    bDelta = int((endColor[2] - startColor[2]) / totalTime)
    color = list(startColor)
    for i in range(0, totalTime):
        print(color)
        color[0] += rDelta
        color[1] += gDelta
        color[2] += bDelta
        applyToAll(color)
        pixels.show()
        time.sleep(.001)

def transitionSectionsToColor(startColor0, endColor0, startColor1, endColor1, startColor2, endColor2, totalTime):
    rDelta0 = int((endColor0[0] - startColor0[0]) / totalTime)
    gDelta0 = int((endColor0[1] - startColor0[1]) / totalTime)
    bDelta0 = int((endColor0[2] - startColor0[2]) / totalTime)
    rDelta1 = int((endColor1[0] - startColor1[0]) / totalTime)
    gDelta1 = int((endColor1[1] - startColor1[1]) / totalTime)
    bDelta1 = int((endColor1[2] - startColor1[2]) / totalTime)
    rDelta2 = int((endColor2[0] - startColor2[0]) / totalTime)
    gDelta2 = int((endColor2[1] - startColor2[1]) / totalTime)
    bDelta2 = int((endColor2[2] - startColor2[2]) / totalTime)
    color0 = list(startColor0)
    color1 = list(startColor1)
    color2 = list(startColor2)
    for i in range(0, totalTime):
        color0[0] += rDelta0
        color0[1] += gDelta0
        color0[2] += bDelta0
        color1[0] += rDelta1
        color1[1] += gDelta1
        color1[2] += bDelta1
        color2[0] += rDelta2
        color2[1] += gDelta2
        color2[2] += bDelta2
        applyToSection(section1, color0)
        applyToSection(section2, color1)
        applyToSection(section3, color2)
        pixels.show()
        time.sleep(.001)
############################################################################
############################################################################
############################################################################
############################################################################
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(3):
            pixel_index = (i * 256 // 3) + j
            applyToSection(sections[i], wheel(pixel_index&255))
            #pixels[sections[i]] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def pingpongAll(startingColor, endColor, time):
    print("pingAll")
    transitionAllToColor(startingColor, endColor, time)
    print("pongAll")
    transitionAllToColor(endColor, startingColor, time)

def pingpongSections(sColor1, eColor1, sColor2, eColor2, sColor3, eColor3, time):
    print("pingSections")
    transitionSectionsToColor(sColor1,eColor1,sColor2,eColor2,sColor3,eColor3,time)
    print("pongSections")
    transitionSectionsToColor(eColor1,sColor1,eColor2,sColor2,eColor3,sColor3,time)

while True:
    pixels.fill((125,255,0))
    pixels.show()
    time.sleep(1)
    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
    pingpongAll((255,0,0), (0,255,0), 1000)
    pingpongSections( (255, 0, 0), (0,255, 0),
        (125,0,0), (0, 255, 0),
        (0,0,0), (0, 255, 0),
        1000
        )



