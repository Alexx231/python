from turtle import *
import colorsys

bgcolor("black")
pensize(4)
tracer(10)
h=0

def dibujo(a,n):
    circle(5+n,60), left(a), circle(5+n,60)
    
for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.008
    color(c, "black"), begin_fill()
    dibujo(90, i/2), end_fill()
    dibujo(160,i*1.2), penup()
    dibujo(0,0), dibujo(90,i/2), pendown()
    
done()