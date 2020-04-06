import board
import neopixel
import time

pixel_pin = board.D18
num_pixels = 12
print(dir(neopixel))
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, pixel_order=ORDER)
# pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

#for i in range(12):
 #  print(i)

i=2

#Red 1 is on
pixels[0] = (255, 255, 255)
time.sleep(1)

pixels[1] = (255, 255, 255)
time.sleep(1)

pixels[2] = (255, 255, 255)
time.sleep(1)

pixels[3] = (255, 0, 0)
time.sleep(1)

pixels[4] = (255, 0, 0)
time.sleep(1)

pixels[5] = (255, 0, 0)
time.sleep(1)

pixels[6] = (255, 0, 0)
time.sleep(1)

pixels[7] = (255, 0, 0)
time.sleep(1)

pixels[8] = (255, 0, 0)
time.sleep(1)

pixels[9] = (255, 0, 0)
time.sleep(1)

pixels[10] = (255, 0, 0)
time.sleep(1)

pixels[11] = (255, 0, 0)
time.sleep(1)


   #Red is on
#   pixels[i] = (0, 255, 0, 0)
#   time.sleep(0.5)

   #blue is on
#   pixels[i] = (0, 0, 255, 0)
#   time.sleep(0.5)

   #White is on
 #  pixels[i] = (0, 0, 0, 255)
 #  time.sleep(0.5)

#pixels[i] = (0, 0, 0, 0)




