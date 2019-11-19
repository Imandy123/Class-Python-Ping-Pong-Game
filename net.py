class Net(pygame.sprite.Sprite):
      def __init__(self, x, y):
           pygame.sprite.Sprite.__init__(self)
           self.image = pygame.Surface((300, 5))
           pygame.draw.line(self.image, (255, 255, 255),(400, 395),(700, 395), 5)
           self.rect = self.image.get_rect()
           self.rect.x = x
           self.rect.y = y
           self.rapos = random.randrange(300, 1091)

    
       def move(self, speed):
           if(self.rapos < self.rect.right): 
               if(self.rect.right - self.rapos < speed): 
                  self.rect.right -= 1
               else:
                  self.rect.right -= speed                   
           elif(self.rapos > self.rect.right):
               if(self.rapos - self.rect.right < speed): 
                  self.rect.right += 1
               else:
                  self.rect.right += speed
           else:
                self.rapos = random.randrange(300, 1091)

