import pygame
class Button(pygame.sprite.Sprite):
      
      def __init__(self, name, pos, image, altimg):
          pygame.sprite.Sprite.__init__(self) 
          self.name = name
          self.images = [pygame.image.load("button.png"), pygame.image.load(altimg)]
          self.image = self.images[0] 
          self.rect = self.image.get_rect()
          self.rect.x = pos[0]
          self.rect.y = pos[1]
     
      def clicked(self, mospos): #Checks if mouse clicks button, changes image slightly and returns boolean
          if mospos == self.rect.center:
             self.image = self.images[1]
             self.rect = self.image.get_rect()
             self.screen.blit(self.image)
             return True
