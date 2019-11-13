class Flag(pygame.sprite.Sprite):
      
      def __init__(self, name, pos, image):
          pygame.sprite.Sprite.__init__(self) 
          self.name = name
          self.image = pygame.image.load("flag.png")
          self.rect = self.image.get_rect()
          self.rect.x = pos[0]
          self.rect.y = pos[1]

       def caption(self, name):
           myfont = pygame.font.SysFont(None, 50)
           message = myfont.render(name, False, (0,0,0))
           self.screen.blit(message, (0, 0))
