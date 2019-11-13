class Flag(pygame.sprite.Sprite):
      
      def __init__(self, name, pos, image):
          pygame.sprite.Sprite.__init__(self) 
          self.name = name
          self.image = pygame.image.load(image)
          self.rect = self.image.get_rect()
          self.rect.x = pos[0]
          self.rect.y = pos[1]
