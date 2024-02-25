from pygame import *

background_color = (200, 255, 255)
window_width = 600
window_height = 500
window = display.set_mode((window_width, window_height))
window.fill(background_color)
 
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_width, sprite_height, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (sprite_width, sprite_height))
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        self.speed = sprite_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < window_height - 80:
            self.rect.y += self.speed
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_height - 80:
            self.rect.y += self.speed

font.init()
font = font.Font(None, 35)

loseOne = font.render('Player one lose', True, (180, 0, 0))
loseTwo = font.render('Player two lose', True, (180, 0, 0))

racketOne = Player('racket.png', 30, 200, 50, 150, 4)
racketTwo = Player('racket.png', 520, 200, 50, 150, 4)

ball = GameSprite('tennis_ball.png', 200, 200, 50, 50, 4)

speed_x = 3
speed_y = 3

game = True
finish = False
clock = time.Clock()
FPS = 60
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
  
    if finish != True:
        window.fill(background_color)
        racketOne.update_left()
        racketTwo.update_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > window_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(loseOne, (200, 200))
        if ball.rect.x > window_width:
            finish = True
            window.blit(loseTwo, (200, 200))
        if sprite.collide_rect(racketOne, ball) or sprite.collide_rect(racketTwo, ball):
            speed_x *= -1
            speed_y *= 1
        racketOne.reset()
        racketTwo.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
