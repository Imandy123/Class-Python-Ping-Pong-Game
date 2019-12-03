import pygame
import random
class Net(pygame.sprite.Sprite):
    def __init__(self, x, y, swidth):
        pygame.sprite.Sprite.__init__(self)
        self.finPos = swidth
        self.image = pygame.Surface((300, 10))
        self.image.fill((255,255,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.raPos = random.randrange(300, self.finPos+1)

    
    def move(self, speed):
           if(self.raPos < self.rect.right): 
               if(self.rect.right - self.raPos < speed): 
                  self.rect.right -= 1
               else:
                  self.rect.right -= speed                   
           elif(self.raPos > self.rect.right):
               if(self.raPos - self.rect.right < speed): 
                  self.rect.right += 1
               else:
                  self.rect.right += speed
           else:
                self.raPos = random.randrange(300, self.finPos+1)
