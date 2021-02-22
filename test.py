import board
import neopixel
import time

maxPixels = 12
pixels = neopixel.NeoPixel(board.D18, maxPixels)

back = [0,1,2,3,4,5,6,7,8,9,10,11]
mid = [12,13,14,15,16,17,18,19,20,21,22,23]
front = [24,25,26,27,28,29,30,31,32,33,34,35]

left = [0,1,2,3,4,19,20,21,22,23,24,25,26,27,28]
middle = [5,6,17,18,29,30]
right = [7,8,9,10,11,12,13,14,15,16,31,32,33,34,35]

top = [0,1,10,11,12,13,22,23,24,25,34,35]
center = [2,3,8,9,14,15,20,21,26,27,32,33]
bot = [4,5,6,7,16,17,18,19,28,29,30,31]

sections = [back, mid, front]

def setInBoundary(col):
	if(col > 255):
		return 255
	if(col < 0):
		return 0
	return col

def colorAll(array, color):
	for pNumber in array:
		if pNumber < maxPixels:
			pixels[pNumber] = color


j=0
directionUp = True


while True:
	for i in range(0, maxPixels):
		r = j
		g = 0
		b = 255-j
	colorAll(top, (r,g,b))
	colorAll(center, (r,g,b))
	colorAll(bot, (r,g,b))

	if(directionUp):
		j += 1
		if(j > 255):
			j -= 1
			directionUp = False
	else:
		j -= 1
		if(j < 0):
			j += 1
			directionUp = True
	time.sleep(.001)