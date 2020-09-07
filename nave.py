import pygame


class Nave(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/personagens/Nave.png")
        self.image = pygame.transform.scale(self.image, [110, 70])
        self.rect = pygame.Rect(50, 200, 100, 100)
        self.speed = 0
        self.acceleration = 0.1

    def update(self, *args):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_d]:
            self.rect.x += 3
        elif keys[pygame.K_a]:
            self.rect.x -= 3
        if keys[pygame.K_s]:
            self.rect.y += 3
        elif keys[pygame.K_w]:
            self.rect.y -= 3

        elif keys[pygame.K_LSHIFT]:

            if keys[pygame.K_d]:
                self.rect.x += 5
            elif keys[pygame.K_a]:
                self.rect.x -= 5

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speed = 0
