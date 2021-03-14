from math import sin,cos,pi
from pyautocad import Autocad,APoint

cad=Autocad()
nktalar=list()
kenar=1000          #Eşkenar altıgenin bir kenarının uzunluğu
p0x=10              #Başlangıç noktasının x koordinatı
p0y=10              #Başlangıç noktasının y koordinatı
p0=APoint(p0x,p0y)
p1=APoint(p0.x+kenar,p0.y)
p2=APoint(p1.x+kenar*cos(60*(pi/180)),p1.y+kenar*sin(60*(pi/180)))
p3=APoint(p2.x-kenar*cos(60*(pi/180)),p2.y+kenar*sin(60*(pi/180)))
p4=APoint(p3.x-kenar,p3.y)
p5=APoint(p4.x-kenar*cos(60*(pi/180)),p4.y-kenar*sin(60*(pi/180)))



cad.model.addline(p0,p1)
cad.model.addline(p1,p2)
cad.model.addline(p2,p3)
cad.model.addline(p3,p4)
cad.model.addline(p4,p5)
cad.model.addline(p5,p0)
