import pygame 
import random
SCREEN_WIDTH, SCREEN_HEIGHT=500,400
MOVEMENT_SPEED=5
FONT_SIZE=72
pygame.init()
bg_image=pygame.transform.scale(pygame.image.load("123.jpg"),
(SCREEN_WIDTH,SCREEN_HEIGHT))
font=pygame.font.SysFont("Times New Roman",FONT_SIZE)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.Color("dodgerblue"))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0 ,width, height))
        self.rect=self.image.get_rect()
    def move(self,x_change,y_change):
        self.rect.x=max(
            min(self.rect.x+x_change,SCREEN_WIDTH=self.rect.width),0
        ) 
        self.rect.y=max (min(self.rect.y+y_change,SCREEN_WIDTH=self.rect.height),0
        )    
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites=pygame.sprite.Group()
s1=Sprite(pygame.color("black"), 50,35)
s1.rect.x,s1.rect.y=random.randint(
    0, SCREEN_WIDTH -s1.rect.width),random.randint(
        0,SCREEN_HEIGHT -s1.rect.height)
all_sprites.add(s1)
s2=Sprite(pygame.color("red"), 50,35)
s2.rect.x,s2.rect.y=random.randint(
    0, SCREEN_WIDTH -s2.rect.width),random.randint(
        0,SCREEN_HEIGHT -s2.rect.height)
all_sprites.add(s2)
running, won=True,False
clock=pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT or (event.type==pygame.KEYDOWN
        and event.key==pygame.K_x):
         running= False
    if not won:
      keys=pygame.key.get_pressed()
      x_change=(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*MOVEMENT_SPEED
      y_change=(keys[pygame.K_UP]-keys[pygame.K_DOWN])*MOVEMENT_SPEED
      s1.move(x_change,y_change)
      if s1.rect.colliderect(s2.rect):
        all_sprites.remove(s2)
        won=True
    screen.blit(bg_image,(0,0))
    all_sprites.draw(screen)
    if won:
      win_text=font.render("You Won!",True,pygame.color("black"))
      screen.blit(win_text,((SCREEN_WIDTH-win_text.get_width())//2,
     (SCREEN_HEIGHT-win_text.get_height())//2))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()    





    





