import pyautocad as pau
import math as mt
import numpy as np
acad=pau.Autocad()
r1=100
r2=10
acı=22.5
for i in np.arange(0,360,acı):
    px=r1*mt.cos((i*mt.pi)/180)
    py=r1*mt.sin((i*mt.pi)/180)
    p=pau.APoint(px,py)
    acad.model.addcircle(p,r2)