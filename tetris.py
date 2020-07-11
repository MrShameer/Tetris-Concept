import math
import time
import random
from tkinter import *

master = Tk()
w = Canvas(master, width=370, height=550)
w.pack()
LOOP_ACTIVE = True
for i in range(10):
	w.create_rectangle(i*30+50,20,i*30+80,50,outline="black", fill="gray")
	w.create_rectangle(i*30+50,500,i*30+80,530,outline="black", fill="gray")
	
for i in range(17):
	w.create_rectangle(20,i*30+20,50,i*30+50,outline="black", fill="gray")
	w.create_rectangle(320,i*30+20,350,i*30+50,outline="black", fill="gray")

move=0
sec=0.5
def key_pressed(event):
	global move
	global sec
	if event.char == 'd':
		move+=30
	elif event.char == 'a':
		move-=30
	elif event.char == 's':
		sec=0.1
master.bind("<Key>",key_pressed)

def Oricky():
  #
###
	for i in range(14):
		b1=w.create_rectangle(200+move,i*30+50,230+move,i*30+80,outline="black", fill="orange")
		b2=w.create_rectangle(140+move,i*30+80,170+move,i*30+110,outline="black", fill="orange")
		b3=w.create_rectangle(170+move,i*30+80,200+move,i*30+110,outline="black", fill="orange")
		b4=w.create_rectangle(200+move,i*30+80,230+move,i*30+110,outline="black", fill="orange")
		master.update()
		time.sleep(sec)
		w.delete(b1)
		w.delete(b2)
		w.delete(b3)
		w.delete(b4)
		if i==13:
			w.create_rectangle(200+move,i*30+50,230+move,i*30+80,outline="black", fill="orange")
			w.create_rectangle(140+move,i*30+80,170+move,i*30+110,outline="black", fill="orange")
			w.create_rectangle(170+move,i*30+80,200+move,i*30+110,outline="black", fill="orange")
			w.create_rectangle(200+move,i*30+80,230+move,i*30+110,outline="black", fill="orange")

def hero():
####
	for i in range(15):
		b1=w.create_rectangle(140+move,i*30+50,170+move,i*30+80,outline="black", fill="cyan")
		b2=w.create_rectangle(230+move,i*30+50,260+move,i*30+80,outline="black", fill="cyan")
		b3=w.create_rectangle(170+move,i*30+50,200+move,i*30+80,outline="black", fill="cyan")
		b4=w.create_rectangle(200+move,i*30+50,230+move,i*30+80,outline="black", fill="cyan")
		master.update()
		time.sleep(sec)
		w.delete(b1)
		w.delete(b2)
		w.delete(b3)
		w.delete(b4)
		if i==14:
			w.create_rectangle(140+move,i*30+50,170+move,i*30+80,outline="black", fill="cyan")
			w.create_rectangle(230+move,i*30+50,260+move,i*30+80,outline="black", fill="cyan")
			w.create_rectangle(170+move,i*30+50,200+move,i*30+80,outline="black", fill="cyan")
			w.create_rectangle(200+move,i*30+50,230+move,i*30+80,outline="black", fill="cyan")

def Bricky():
#
###
	for i in range(14):
		b1=w.create_rectangle(140+move,i*30+50,170+move,i*30+80,outline="black", fill="blue")
		b2=w.create_rectangle(140+move,i*30+80,170+move,i*30+110,outline="black", fill="blue")
		b3=w.create_rectangle(170+move,i*30+80,200+move,i*30+110,outline="black", fill="blue")
		b4=w.create_rectangle(200+move,i*30+80,230+move,i*30+110,outline="black", fill="blue")
		master.update()
		time.sleep(sec)
		w.delete(b1)
		w.delete(b2)
		w.delete(b3)
		w.delete(b4)
		if i==13:
			w.create_rectangle(140+move,i*30+50,170+move,i*30+80,outline="black", fill="blue")
			w.create_rectangle(140+move,i*30+80,170+move,i*30+110,outline="black", fill="blue")
			w.create_rectangle(170+move,i*30+80,200+move,i*30+110,outline="black", fill="blue")
			w.create_rectangle(200+move,i*30+80,230+move,i*30+110,outline="black", fill="blue")

def cleveland():
##
 ##
	for i in range(14):
		b1=w.create_rectangle(170+move,i*30+50,200+move,i*30+80,outline="black", fill="red")
		b2=w.create_rectangle(200+move,i*30+50,230+move,i*30+80,outline="black", fill="red")
		b3=w.create_rectangle(230+move,i*30+80,260+move,i*30+110,outline="black", fill="red")
		b4=w.create_rectangle(200+move,i*30+80,230+move,i*30+110,outline="black", fill="red")
		master.update()
		time.sleep(sec)
		w.delete(b1)
		w.delete(b2)
		w.delete(b3)
		w.delete(b4)
		if i==13:
			w.create_rectangle(170+move,i*30+50,200+move,i*30+80,outline="black", fill="red")
			w.create_rectangle(200+move,i*30+50,230+move,i*30+80,outline="black", fill="red")
			w.create_rectangle(230+move,i*30+80,260+move,i*30+110,outline="black", fill="red")
			w.create_rectangle(200+move,i*30+80,230+move,i*30+110,outline="black", fill="red")

def rhode():
 ##
##
	for i in range(14):
		b1=w.create_rectangle(170+move,i*30+50,200+move,i*30+80,outline="black", fill="green")
		b2=w.create_rectangle(200+move,i*30+50,230+move,i*30+80,outline="black", fill="green")
		b3=w.create_rectangle(170+move,i*30+80,200+move,i*30+110,outline="black", fill="green")
		b4=w.create_rectangle(140+move,i*30+80,170+move,i*30+110,outline="black", fill="green")
		master.update()
		time.sleep(sec)
		w.delete(b1)
		w.delete(b2)
		w.delete(b3)
		w.delete(b4)
		if i==13:
			w.create_rectangle(170+move,i*30+50,200+move,i*30+80,outline="black", fill="green")
			w.create_rectangle(200+move,i*30+50,230+move,i*30+80,outline="black", fill="green")
			w.create_rectangle(170+move,i*30+80,200+move,i*30+110,outline="black", fill="green")
			w.create_rectangle(140+move,i*30+80,170+move,i*30+110,outline="black", fill="green")

def teewee():
 #
###
	for i in range(14):
		b1=w.create_rectangle(170+move,i*30+50,200+move,i*30+80,outline="black", fill="purple")
		b2=w.create_rectangle(140+move,i*30+80,170+move,i*30+110,outline="black", fill="purple")
		b3=w.create_rectangle(170+move,i*30+80,200+move,i*30+110,outline="black", fill="purple")
		b4=w.create_rectangle(200+move,i*30+80,230+move,i*30+110,outline="black", fill="purple")
		master.update()
		time.sleep(sec)
		w.delete(b1)
		w.delete(b2)
		w.delete(b3)
		w.delete(b4)
		if i==13:
			w.create_rectangle(170+move,i*30+50,200+move,i*30+80,outline="black", fill="purple")
			w.create_rectangle(140+move,i*30+80,170+move,i*30+110,outline="black", fill="purple")
			w.create_rectangle(170+move,i*30+80,200+move,i*30+110,outline="black", fill="purple")
			w.create_rectangle(200+move,i*30+80,230+move,i*30+110,outline="black", fill="purple")

def smashboy():
	##
	##
	for i in range(14):
		b1=w.create_rectangle(170+move,i*30+50,200+move,i*30+80,outline="black", fill="#fb0")
		b2=w.create_rectangle(200+move,i*30+50,230+move,i*30+80,outline="black", fill="#fb0")
		b3=w.create_rectangle(170+move,i*30+80,200+move,i*30+110,outline="black", fill="#fb0")
		b4=w.create_rectangle(200+move,i*30+80,230+move,i*30+110,outline="black", fill="#fb0")
		master.update()
		time.sleep(sec)
		w.delete(b1)
		w.delete(b2)
		w.delete(b3)
		w.delete(b4)
		if i==13:
			w.create_rectangle(170+move,i*30+50,200+move,i*30+80,outline="black", fill="#fb0")
			w.create_rectangle(200+move,i*30+50,230+move,i*30+80,outline="black", fill="#fb0")
			w.create_rectangle(170+move,i*30+80,200+move,i*30+110,outline="black", fill="#fb0")
			w.create_rectangle(200+move,i*30+80,230+move,i*30+110,outline="black", fill="#fb0")


while LOOP_ACTIVE:
	move=0
	sec=0.5
	block = random.randint(0,7)
	if block==0:
		Oricky()
	elif block==1:
		hero()
	elif block==2:
		Bricky()
	elif block==3:
		cleveland()
	elif block==4:
		rhode()
	elif block==5:
		smashboy()
	else:
		teewee()
	#LOOP_ACTIVE=False


	
