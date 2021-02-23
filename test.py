import board
import neopixel
import time

maxPixels = 12
pixelsPin = board.D18
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(pixelsPin, maxPixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

back = [0,1,2,3,4,5,6,7,8,9,10,11]
mid = [12,13,14,15,16,17,18,19,20,21,22,23]
front = [24,25,26,27,28,29,30,31,32,33,34,35]

left = [0,1,2,3,4,19,20,21,22,23,24,25,26,27,28]
middle = [5,6,17,18,29,30]
right = [7,8,9,10,11,12,13,14,15,16,31,32,33,34,35]

top = [0,1,10,11,12,13,22,23,24,25,34,35]
center = [2,3,8,9,14,15,20,21,26,27,32,33]
bot = [4,5,6,7,16,17,18,19,28,29,30,31]

sections = top + center + bot
toRemove = []

for i in sections:
	if i >= maxPixels:
		toRemove.append(i)
for i in toRemove:
	sections.remove(i)

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
 
 
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(maxPixels):
            pixel_index = (i * 256 // maxPixels) + j
            pixels[sections[i]] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
 
 
while True:
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((255, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0, 0))
    pixels.show()
    time.sleep(1)
 
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0, 0))
    pixels.show()
    time.sleep(1)
 
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 0, 255))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255, 0))
    pixels.show()
    time.sleep(1)
 
    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step