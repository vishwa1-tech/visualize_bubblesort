import pygame
import sys
import random
import time

WIDTH= 800
HEIGHT= 600

num_bars=100
bar_width=5
space=1
sorting=False
bars=[]

blue=(0,0,255)

pygame.init()
screen= pygame.display.set_mode((WIDTH,HEIGHT))
font=pygame.font.SysFont('Arial', 30)
clock=pygame.time.Clock()
screen.fill((255,255,255)) 


def bubbleSort(arr):
	elapsed=clock.tick(1)


	n=len(arr)
	for i in range(n):
		for j in range(0,n-1-i):

			for k in range(num_bars):
				x =(k * bar_width) + (k * space) +(WIDTH -(num_bars *bar_width +num_bars *space))/2
				height=bars[k]

				if bars[k] is bars[j] or bars[k] is bars[j+1]:
					color=(255,130,88)
				else:
					color=blue

				drawBar(x,height,color)
			pygame.display.update()
			time.sleep(.001)

			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]= arr[j+1],arr[j]
			screen.fill((255,255,255))
 
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()


def button(msg,x,y,w,h,ic,ac):
	mouse=pygame.mouse.get_pos()
	click=pygame.mouse.get_pressed()
	global sorting

	if x+w>mouse[0]>x and y+h>mouse[1]>y:
	    pygame.draw.rect(screen,ac,(x,y,w,h),0)

	    if click[0] == 1:
	    	sorting=True
 
	else:
		pygame.draw.rect(screen,ic,(x,y,w,h),0)

	text=font.render(msg,True,(0,0,0))
	screen.blit(text,(x+10,y+10))



def drawBar(x,height,color):
	pygame.draw.rect(screen,color,(x,400,bar_width,height),0)
	bars.append(height)

for i in range(num_bars):
	height=random.randint(-100,-10)
	x = (i * bar_width) + (i *space)+(WIDTH - (num_bars*bar_width+num_bars*space))/2
	drawBar(x,height,blue)

while True:
    button('Sorted part', 200-75/2, 200-25, 75 , 50, (230,230,230),(200,200,200))
    
    pygame.display.update()

    if sorting:
    	break

    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    		pygame.quit()
    		sys.exit()


bubbleSort(bars)

