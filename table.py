class Table(pygame.sprite.Sprite):
      
      def __init__(self, name, pos, image):
          pygame.sprite.Sprite.__init__(self) 
          self.name = name
          self.image = pygame.image.load(image)
          self.rect = self.image.get_rect()
          self.rect.x = pos[0]
          self.rect.y = pos[1]
  
      def ballOn(self, ball):
          if ball.rect.y > self.rect.y or ball.rect.y < self.rect.y:
             return False
          else:
             return True
      
      def paddleNear(self, paddle):
          if paddle.rect.x > self.rect.x or paddle.rect.x < self.rect.x:
             return False
          else:
             return True


    
