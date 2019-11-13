class Paddle(pygame.sprite.Sprite):
      
      def __init__(self, player, pos, image):
          pygame.sprite.Sprite.__init__(self) 
          self.player = player
          self.image = pygame.image.load("paddle.png")
          self.rect = self.image.get_rect()
          self.rect.x = pos[0]
          self.rect.y = pos[1]
          self.opScore = 0
          self.score = 0
      
      def comp(self, ball, table, collisions): #Opponent
          while self.opScore < self.score:
                self.rect.x = ball.rect.x
                if ball.rect.y < self.rect.y:
                   self.score += 1
                if self.opScore == 11:
                   self.score = 12
          ball.speedUp(collisions)
          ball.bounce(table)


      def play(self, ball, table, collisions): #You
          while self.score > self.opScore:
                self.rect.center = pygame.mouse.get_pos()
                if ball.rect.y > self.rect.y:
                   self.opScore += 1
                if self.score == 11:
                   self.opScore = 12
          ball.speedUp(collisions)
          ball.bounce(table)
          
