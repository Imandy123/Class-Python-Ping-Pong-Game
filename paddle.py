class Paddle(pygame.sprite.Sprite):
      
      def __init__(self, player, pos, image):
          pygame.sprite.Sprite.__init__(self) 
          self.player = player
          self.image = pygame.image.load(image)
          self.rect = self.image.get_rect()
          self.rect.x = pos[0]
          self.rect.y = pos[1]
      
      def comp(self, ball, table): #Opponent


      def play(self, ball, table): #You
          
