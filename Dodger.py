#Dodger
import pygame 
import random
pygame.init()

WHITE=(255,255,255)
W=600
H=600
clock=pygame.time.Clock()
FPS=60

sc=pygame.display.set_mode((W,H))
sc.fill(WHITE)

pygame.display.set_caption('Dodger')

icon=pygame.image.load('C:/Users/A/Desktop/Dodger/icon.png')
pygame.display.set_icon(icon)

pygame.mixer.music.load('C:/Users/A/Desktop/Новая папка (3)/Новая папка (2)/Kalimba.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

player_x=W//2
player_y=500
a=0

class Enemy(pygame.sprite.Sprite):
	
	def __init__(self,scale,rect):
		self.image=pygame.image.load('C:/Users/A/Desktop/Dodger/enemy.png')
		self.scale=rect
		self.rect=self.image.get_rect(center=(scale))
		sc.blit(self.image,self.rect)
	def draw(self):
		size=pygame.transform.scale(self.image,(self.scale))
		sc.blit(self.image,self.rect)

enemy_x=random.randint(0,600)
enemy_y=0

enemy2_x=random.randint(0,600)
enemy2_y=0

enemy3_x=random.randint(0,600)
enemy3_y=0

enemy_count=0
immortal=0
dead=0
pygame.display.update()

while 1:
	sc.fill(WHITE)
	
	if dead!=1:
		enemy_y+=random.randint(3,15)
		enemy2_y+=random.randint(3,15)
		enemy3_y+=random.randint(3,15)
	
	enemy=Enemy((enemy_x,enemy_y),(0,600))
	
	enemy2=Enemy((enemy2_x,enemy2_y),(0,600))
	
	enemy3=Enemy((enemy3_x,enemy3_y),(0,600))
		
	if enemy_count<=1:	
		enemy.draw()
		enemy2.draw()
		enemy3.draw()
		enemy_count+=1

	image = pygame.image.load('C:/Users/A/Desktop/Dodger/player.png').convert_alpha()
	rect = image.get_rect(center=(player_x, player_y))
	sc.blit(image,rect)
	
	for i in pygame.event.get():
		if i.type==pygame.QUIT:
			pygame.quit()
			break


	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and player_x>0 and dead!=1:
		player_x -= 3
	if keys[pygame.K_RIGHT] and player_x<600 and dead!=1:
		player_x += 3
	if keys[pygame.K_UP] and player_y>0 and dead!=1:
		player_y -= 3  
	if keys[pygame.K_DOWN] and player_y<600 and dead!=1:
		player_y += 3  

	if dead!=1:
		f1=pygame.font.SysFont('impact',24)
		text=f1.render('Счёт: '+str(a),1,(63,72,204))
		sc.blit(text, (500,5))
		a+=1


	if rect.colliderect(enemy.rect) and immortal!=1:
		image = pygame.image.load('C:/Users/A/Desktop/Dodger/dead_player.png').convert_alpha()
		dead=1
		sc.blit(image,rect)
	if rect.colliderect(enemy2.rect) and immortal!=1:
		image = pygame.image.load('C:/Users/A/Desktop/Dodger/dead_player.png').convert_alpha()
		dead=1
		sc.blit(image,rect)
	if rect.colliderect(enemy3.rect) and immortal!=1:
		image = pygame.image.load('C:/Users/A/Desktop/Dodger/dead_player.png').convert_alpha()
		dead=1
		sc.blit(image,rect)


	if a>=1000 and a<1500:
		immortal=1
		image = pygame.image.load('C:/Users/A/Desktop/Dodger/immortal_player.png').convert_alpha()
		sc.blit(image,rect)
	else:
		immortal=0


	if dead==1:
		f2=pygame.font.SysFont('impact',34)
		text2=f2.render('Игра окончена!',1,(63,72,204))
		text3=f2.render('Ваш счёт:'+ str(a),1,(63,72,204))
		sc.blit(text2, ((W//2)-100,H//2))
		sc.blit(text3, ((W//2)-90,(H//2)+40))

	if enemy_y>=600:
		enemy_x=random.randint(0,600)
		enemy_y=0
		enemy_count-=1
	if enemy2_y>=600:
		enemy_x=random.randint(0,600)
		enemy2_y=0
		enemy_count-=1
	if enemy3_y>=600:
		enemy_x=random.randint(0,600)
		enemy3_y=0
		enemy_count-=1

	clock.tick(FPS)
	pygame.display.update()
