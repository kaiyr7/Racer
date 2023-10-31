import pygame
import random
pygame.init()

screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("RACER")
run=True
clock=pygame.time.Clock()
x=400
#loading all images
background=pygame.image.load('lab8/Racer/background1.png').convert_alpha()
car=pygame.image.load('lab8/Racer/car.png').convert_alpha()
enemy=pygame.image.load('lab8/Racer/enemy.png').convert_alpha()
coin=pygame.image.load('lab8/Racer/tenge.png').convert_alpha()

#variables
bg_y=0
enemy_y=-5
enemy_x=random.randint(64,800-190)
coin_x=random.randint(64,800-190)
coin_y=0
score=0
#making font variable from modules
font = pygame.font.SysFont("classic", 80)
speed=7
#coef is for the size of coin
coef=1
miss=0

while run:
    #if event is quit stop the loop by turning run to false
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and x>64: x -= 15
    if pressed[pygame.K_RIGHT] and x<800-189: x += 15
    #bg_y is coordinates of background by y and increase speed is increase of it
    bg_y+=speed//1.5
    #two same background images are changing so they make animation of movement
    #if coordinate went above 800 i reset it so my road will be infinite
    if bg_y>800:
        bg_y=0
    #enemy is moving by adding units like background but 1.5x faster
    enemy_y+=speed
    #if enemy passed all the way I reset coordinate but with random possition by x
    if enemy_y>800:
        enemy_y=-5
        enemy_x=random.randint(64,800-189)
    coin_y+=speed//1.5
    #coin is moving with background

    #like enemy if coin passed all the way I reset coordinate but with random possition by x
    #and transform scale by random coef time of original size
    # if coin passed all the way I also add 1 miss
    if coin_y>800:
        coin_y=0
        coin_x=random.randint(64,800-189)
        coef=random.randint(1,3)
        coin=pygame.transform.scale(coin,(64*coef,64*coef))
        miss+=1
    
    #two background and enemy,car,coin bliting on the screen with changing coordinates
    screen.blit(background,(0,bg_y))
    screen.blit(background,(0,bg_y-800))
    screen.blit(car,(x,800-140))
    screen.blit(enemy,(enemy_x,enemy_y))
    screen.blit(coin,(coin_x,coin_y))

    #making two texts on the screen
    #first one on the right upper corner is score and on the left upper corner is misses
    text=font.render(str(score),True,'Gold')
    screen.blit(text,(800-64,0+32))
    text2=font.render('X'*miss,True,'Red')
    screen.blit(text2,(0,0))
    
    #making rectangles of images
    car_rect=car.get_rect(topleft=(x,800-140))
    enemy_rect=enemy.get_rect(topleft=(enemy_x,enemy_y))
    coin_rect=coin.get_rect(topleft=(coin_x,coin_y))

    #by method colliderect if two rectangles collide do certain things

    if car_rect.colliderect(enemy_rect):
        print("GAME OVER")
        print("YOUR SCORE:",score)
        break

    #if car collide coin, reset coin coordinates and change to random size
    #increase the speed, add to score depending on size of coin units
    if car_rect.colliderect(coin_rect):
        score+=coef
        speed+=1
        coin_y=0
        coin_x=random.randint(64,800-189)
        coef=random.randint(1,3)
        coin=pygame.transform.scale(coin,(64*coef,64*coef))

    #if missed coins equals 3 stop the game
    if miss==3:
        print("GAME OVER")
        print("YOUR SCORE:",score)
        break
    
    #update display
    pygame.display.update()
    #to make while loop 60 times per second
    clock.tick(60)