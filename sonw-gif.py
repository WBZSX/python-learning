import pygame
import random
#初始化
pygame.init()
SIZE = (1000,500)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("下雪了")
#加载位图
background = pygame.image.load('snow.jpg')
#定义一个雪花列表
snow = []
for i in range(300):
	x = random.randrange(0,SIZE[0])
	y = random.randrange(0,SIZE[1])
	speedx = random.randint(-1,2)
	speedy = random.randint(3,8)
	snow.append([x,y,speedx,speedy])
done = False
while not done:
	#消息时间循环，判断推出
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	#绘制位图
	screen.blit(background,(0,0))
	#雪花列表循环
	for i in range(len(snow)):
		#绘制雪花的颜色、位置、大小
		pygame.draw.circle(screen,(255,255,255),snow[i][:2],snow[i][3])
		#移动雪花位置（下一次循环起效）
		snow[i][0]+=snow[i][2]
		snow[i][1]+=snow[i][3]
		#如果雪花落出屏幕
		if snow[i][1] > SIZE[1]:
			snow[i][1] = random.randrange(-50,-10)
			snow[i][0] = random.randrange(0,SIZE[0])
	pygame.display.flip()
	clock.tick(2)
pygame.quit()
	
