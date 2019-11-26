import pygame
class Paddle(pygame.sprite.Sprite):
     def __init__(self, name, pos):
        pygame.sprite.Sprite.__init__(self) 
        self.name = name
        self.imageOr = pygame.image.load("assets/paddle.png")
        self.imageOr = pygame.transform.scale(self.imageOr, (90, 100))
        self.imageOr = pygame.transform.rotate(self.imageOr, -20)
        if name == "Opp":
            self.imageOr = pygame.transform.flip(self.imageOr, False, True)
        self.image = self.imageOr.copy()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
     
     def rot(self, angle):
            prevCent = self.rect.center
            self.image = pygame.transform.rotate(self.imageOr, angle)
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.center = prevCent
                
            
     def sync(self, swidth):    
            if self.rect.centerx < swidth:
                self.angle = 120/(swidth)
                if self.name == "Opp":
                    self.rot(-(self.angle*((swidth)-self.rect.centerx)))
                else:
                   self.rot(self.angle*((swidth)-self.rect.centerx))

          
