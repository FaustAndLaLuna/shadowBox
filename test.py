import board
import neopixel
import time
maxPixels = 5
pixels = neopixel.NeoPixel(board.D18, maxPixels)

def setInBoundary(col):
	if(col > 255):
		return 255
	if(col < 0):
		return 0
	return col

j=0
directionUp = True


while True:
	for i in range(0, maxPixels):
		r = 255 - (255 / maxPixels) * i + j
		g = j
		b = (255 / maxPixels) * i
		r = setInBoundary(r)
		g = setInBoundary(g)
		b = setInBoundary(b)
		pixels[i] = (r,g,b)
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