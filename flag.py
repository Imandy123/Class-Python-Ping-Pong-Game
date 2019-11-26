import pygame
class Flag(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/iflag.png")
        self.rect = self.image.get_rect()
        self.rect.x = y
        self.rect.y = y
