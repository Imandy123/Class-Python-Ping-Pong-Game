import pygame
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/ball.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 0
        self.transdown = self.rect.centery + 300
        self.transup = self.rect.centery -300

    def move(self, py, trans, speed):
           if(self.rect.centery < py and self.rect.centery > self.transup): 
              self.rect.centery -= 1
              return True      
           if(self.rect.centery > py and self.rect.centery < self.transdown):
              self.rect.centery += 1
              return True
           else:
              return False


