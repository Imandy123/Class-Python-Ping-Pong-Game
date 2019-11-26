import pygame
import sys
import math
import paddle
import ball
import net

class Controller:
    def __init__(self, width =1090, height=790):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height)) # width and height must be passed as a tuple
        pygame.display.set_caption("Infinity Pong")
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
        self.icon = pygame.image.load('assets/paddle.png')
        pygame.display.set_icon(self.icon)
        self.timage = pygame.image.load("assets/intro.png").convert()
        self.timage = pygame.transform.scale(self.timage, (width, height))
        #self.bgimage = pygame.image.load("bg.png").convert()
        #self.bgimage = pygame.transform.scale(self.bgimage, (width, height))
        self.ping = pygame.mixer.Sound("assets/ping.wav")
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((0, 0, 128))
        #self.background.blit(self.bgimage, (0, 0))
        self.width = width
        self.height = height
        self.bol = False
        self.opbol = False
        self.netbol = False
        self.difficulty = 0
        self.net = net.Net(0, self.height/2, self.width)
        self.userPad = paddle.Paddle("User", (0, height))
        self.opPad = paddle.Paddle("Opp", (0, 0))
        self.ball = ball.Ball(530, 600)
        self.balls = pygame.sprite.GroupSingle(self.ball) 
        self.STATE = "INTRO"
    
    def mainloop(self):
        while True:
            if(self.STATE == "INTRO"):
                self.intro()
            if(self.STATE == "GAME"):
                self.gameloop()
            if(self.STATE == "EXIT"):
                self.endloop()
    
    def intro(self):
            pygame.mixer.music.load('assets/Infinity Pong Theme.mp3')
            pygame.mixer.music.play(-1)  
            while self.STATE == "INTRO":
                        for event in pygame.event.get():
                              if event.type == pygame.QUIT: 
                                pygame.quit()
                                sys.exit()
                              elif event.type == pygame.KEYDOWN:
                                     if(event.key == pygame.K_SPACE):
                                       self.STATE = "GAME"
                        self.screen.blit(self.timage, (0, 0))
                        pygame.display.flip()
                       
    
    def gameloop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load('assets/India Theme.mp3')
        pygame.mixer.music.play(-1)  
        pygame.key.set_repeat(1,50) # 1 = ms delay to start action, 50 = ms repeat delay
        while self.STATE == "GAME":
            self.mospos = pygame.mouse.get_pos()
            if self.mospos[1] > (self.height/2)+60 :
               self.userPad.rect.center = self.mospos
            #if self.ball.rect.centery < (self.height/2)-60:
               # self.opPad.rect.midbottom = self.ball.rect.midtop
               # self.ping.play(0, 500)
               # self.ball.rect.y += 300
            self.opPad.rect.centery = self.userPad.rect.centery/2.5
            self.opPad.rect.centerx = self.userPad.rect.centerx
            self.userPad.sync(self.width)
            self.opPad.sync(self.width)
            self.net.move(1) #adjust as difficulty increases, and also increase size of net
            #self.ball.reset()
            #self.ball.update()
            #self.ball.bounce()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                       self.STATE = "INTRO"
                    elif(event.key == pygame.K_SPACE):
                          self.STATE = "EXIT"

            
            #hits = pygame.sprite.spritecollide(self.userPad, self.balls, False)
            #for i in hits:
            self.hits = pygame.sprite.collide_mask(self.userPad, self.ball)
            if self.hits or self.bol:
                self.opbol = False
                self.bol = self.ball.move(self.userPad.rect.centery, 300, 5)
                self.ping.play(0, 300)
            self.opHits = pygame.sprite.collide_mask(self.opPad, self.ball)
            if self.opHits or self.opbol:
                self.bol = False
                self.opbol = self.ball.move(self.opPad.rect.centery, 300, 5)
                self.ping.play(0, 300)
            self.nethits = pygame.sprite.collide_mask(self.net, self.ball)
            if self.nethits or self.netbol:
                  self.bol = False
                  self.opbol = False
                  self.netbol = self.ball.move(self.net.rect.centery, 300, 5)
            #pygame.sprite.spritecollide(sprite, sprite, True)
            #spritegroup.update()
            #spritegroup.draw(screen)
            self.screen.blit(self.background, (0,0)) #stamps surface
            self.screen.blit(self.ball.image, (self.ball.rect.x, self.ball.rect.y))
            self.screen.blit(self.net.image, (self.net.rect.x, self.net.rect.y) )
            self.screen.blit(self.userPad.image, (self.userPad.rect.x, self.userPad.rect.y))
            self.screen.blit(self.opPad.image, (self.opPad.rect.x, self.opPad.rect.y))
            pygame.display.flip() # more reliably , pygame.display.update() faster
            

    def endloop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load('assets/Infinity Pong Loss Theme.mp3')
        self.userPad.kill()
        myfont = pygame.font.SysFont(None, 100)
        message = myfont.render("Game Over", False, (0,0,0))
        self.screen.blit(message, (self.width/2, self.height/2))
        pygame.display.flip()
        pygame.mixer.music.play()
        while self.STATE == "EXIT":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                       self.STATE = "INTRO"
