from pygame import*
class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)


        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

racket1 = Player("racket.png",30,200,50,150,4)
racket2 = Player("racket.png",520,200,50,150,4)
Ball = GameSprite("tenis_ball.png",200,200,50,50,4)
win_height = 500
win_weight = 600
speed_x = 3
speed_y = 3
font.init()
font = font.Font(None,35)
lose_1 = font.render("Игрок_1 проиграл",True,(200,0,0))
lose_2 = font.render("Игрок_2 проиграл",True,(200,0,0))
back = (255,255,0)
window = display.set_mode((win_weight,win_height))
window.fill(back)
clock = time.Clock()
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        Ball.rect.x += speed_x
        Ball.rect.y += speed_y
        if sprite.collide_rect(racket1,Ball) or sprite.collide_rect(racket2,Ball):
            speed_x *= -1
        if Ball.rect.y > win_height - 50 or Ball.rect.y < 0:
            speed_y *= -1
        if Ball.rect.x < 0:
            finish = True
            window.blit(lose_1,(200,200))
        if Ball.rect.x > win_weight:
            finish = True
            window.blit(lose_2,(200,200))
        racket1.reset()
        racket2.reset()
        Ball.reset()
    display.update()
    clock.tick(60)
