class Ball(pygame.sprite.Sprite):
  
      def __init__(self, name, pos, image):
          pygame.sprite.Sprite.__init__(self) 
          self.name = name
          self.image = pygame.image.load("ball.png")
          self.rect = self.image.get_rect()
          self.rect.x = pos[0]
          self.rect.y = pos[1]
 
      def speedUp(self, collisions):
          if collisions:
             for i in collisions:
                 self.rect.y += 5

      def bounce(self, table):
          if table.rect.center == ball.rect.center:
             self.rect.y -= 5
             self.screen.blit(self.image)
             self.rect.y += 5
             self.screen.blit(self.image)


