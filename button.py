class Button(pygame.sprite.Sprite):
      
      def __init__(self, name, pos, image, altimg):
          pygame.sprite.Sprite.__init__(self) 
          self.name = name
          self.image = pygame.image.load(image)
          self.altimg = pygame.image.load(altimg)
          self.rect = self.image.get_rect()
          self.rect.x = pos[0]
          self.rect.y = pos[1]
     
      def clicked(self, mouse): #Checks if mouse clicks button, changes image slightly and returns boolean
      
