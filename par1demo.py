from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = (150, 150, 150)
b = (0, 0, 255)
r = (255,0,0)
e = (0, 0, 0)
y = (255,255,0)
lb = (33,150,243)
br = (27,94,32)

heart = [
e,e,e,e,e,e,e,e,
e,r,r,e,e,r,r,e,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
e,r,r,r,r,r,r,e,
e,e,r,r,r,r,e,e,
e,e,e,r,r,e,e,e,
]

cry_face = [
w,w,y,y,y,y,w,w,
w,y,y,y,y,y,y,w,
y,y,e,y,y,e,y,y,
y,y,lb,y,y,lb,y,y,
y,y,lb,y,y,lb,y,y,
y,y,y,e,e,y,y,y,
w,y,y,y,y,y,y,w,
w,w,y,y,y,y,w,w,
]

flower = [
lb,lb,lb,y,y,lb,lb,lb,
lb,lb,y,y,y,y,lb,lb,
lb,y,y,br,br,y,y,lb,
lb,y,y,br,br,y,y,lb,
lb,lb,y,y,y,y,lb,lb,
lb,br,lb,br,br,lb,br,lb,
lb,lb,br,br,br,br,lb,lb,
r,r,r,br,br,r,r,r,
]

while True:
    sleep(3)
    sense.set_pixels(heart)
    sleep(3)
    sense.set_pixels(cry_face)
    sleep(3)
    sense.set_pixels(flower)
