import numpy as np
from PIL import Image

h = 48
w = 32
tab = np.zeros((h,w,3), dtype=np.uint8)
for i in range(h):
    for j in range(w):
        tab[i,j,0] =255 

red = Image.fromarray(tab)
red.save("red.png")

for i in range(h):
    for j in range(w):
        tab[i,j,1] =127 

orange = Image.fromarray(tab)
orange.save("orange.png")
    
for i in range(h):
    for j in range(w):
        tab[i,j,0] =0 
        tab[i,j,1] =127 
        tab[i,j,2] =255 

blue = Image.fromarray(tab)
blue.save("blue.png")
