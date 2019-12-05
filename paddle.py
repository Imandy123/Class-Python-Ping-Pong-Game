import pygame
import random
class Paddle(pygame.sprite.Sprite):
     def __init__(self, name, image, pos):
        pygame.sprite.Sprite.__init__(self) 
        self.name = name
        self.imageOr = pygame.image.load(image)
        self.imageOr = pygame.transform.scale(self.imageOr, (130, 120))
        if self.name == "Opp":
            self.imageOr = pygame.transform.flip(self.imageOr, False, True)
        self.image = self.imageOr.copy()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.points = 0
        self.randy= random.randrange(50, 300)

     
     def rot(self, angle):
            prevCent = self.rect.center
            self.image = pygame.transform.rotate(self.imageOr, angle)
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.center = prevCent
    
     def ai(self,  speed):
             if(self.randy < self.rect.centery): 
               if(self.rect.centery - self.randy < speed): 
                  self.rect.centery -= 1
               else:
                  self.rect.centery -= speed
               return True                   
             elif(self.randy > self.rect.centery):
               if(self.randy - self.rect.centery < speed): 
                  self.rect.centery += 1
               else:
                  self.rect.centery += speed
               return True
             else:
                 self.randy= random.randrange(50, 300)
                 return False

                
            
     def sync(self, swidth):    
                self.angle = 120/(swidth)
                if self.name == "Opp":
                    self.rot(-(self.angle*((swidth/2)-self.rect.centerx)))
                else:
                    self.rot(self.angle*((swidth/2)-self.rect.centerx))
            