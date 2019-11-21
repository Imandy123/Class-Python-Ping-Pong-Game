class Paddle(pygame.sprite.Sprite):
      def __init__(self, name, pos):
          pygame.sprite.Sprite.__init__(self) 
          self.name = name
          self.imageOr = pygame.image.load("paddle.png")
          self.imageOr = pygame.transform.scale(self.imageOr, (90, 100))
          if name == "Opp":
             self.imageOr = pygame.transform.flip(self.imageOr, False, True)
          self.image = self.imageOr.copy()
          self.rect = self.image.get_rect()
          self.rect.x = pos[0]
          self.rect.y = pos[1]
     
      def rot(self, angle):
          prevCent = self.rect.center
          self.image = pygame.transform.rotate(self.imageOr, angle)
          self.rect = self.image.get_rect()
          self.rect.center = prevCent
                
            
      def sync(self, swidth):    
          if self.rect.centerx < swidth/2:
             self.angle = 80
             if self.name == "Opp":
                self.rot(-self.angle)
             else:
                self.rot(self.angle)
          elif self.rect.centerx > swidth/2:
               self.angle = 10
               if self.name == "Opp":
                  self.rot((self.angle))
               else:
                  self.rot(-(self.angle))

          
