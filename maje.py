from turtle import *
import colorsys

speed(1000)
pensize(3)
bgcolor("black")
hue=0.0

col=colorsys.hsv_to_rgb(hue,1,1)
pencolor(col)
hue+=0.005
circle(5-i,100)
lt(80)
circle(5-i,100)
rt(100)
done()