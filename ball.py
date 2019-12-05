import pygame
import math
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/ball.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = pygame.math.Vector2(0, 0)
      
    def vec(self, py, speed):
           if py[1] < self.rect.centery and py[0] > self.rect.centerx: #ball bottom and left
                self.vel = pygame.math.Vector2(-speed*2, speed)
           elif py[1] < self.rect.centery and py[0] < self.rect.centerx: # ball bottom and right
                  self.vel = pygame.math.Vector2(speed*2, speed)
           elif py[1] > self.rect.centery and py[0] < self.rect.centerx: # ball above and right
                  self.vel = pygame.math.Vector2(speed*2, -speed)
           elif py[1] > self.rect.centery and py[0] > self.rect.centerx: #ball above and left
                  self.vel = pygame.math.Vector2(-speed*2, -speed)
           elif py[1] == self.rect.centery and py[0] < self.rect.centerx: #ball horizontal and right
                  self.vel = pygame.math.Vector2(speed, 0)
           elif py[1] == self.rect.centery and py[0] < self.rect.centerx:  #ball horizontal and left
                  self.vel = pygame.math.Vector2(-speed, 0)
           elif py[1] < self.rect.centery and py[0] == self.rect.centerx: #ball vertical and bottom
                  self.vel = pygame.math.Vector2(0, speed)
           elif py[1] > self.rect.centery and py[0] == self.rect.centerx: #ball vertical and top
                  self.vel = pygame.math.Vector2(0, -speed)
           return self.vel
               
   
    def bounce(self, vel):
           #self.vel = pygame.math.Vector2(math.cos(angle)*speed, math.sin(angle)*speed)
           self.rect.center +=  self.vel 
           return True   
           

       