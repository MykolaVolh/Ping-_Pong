from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):  
    def update(self):  
        keys_pressed = key.get_pressed()  
        if keys_pressed [K_DOWN] and self.rect.x > 5 :  
            self.rect.x -= self.speed    

            keys_pressed = key.get_pressed()  
        if keys_pressed [K_UP] and self.rect.x < win_width - 80 :  
            self.rect.x += self.speed 
#Рух вниз для другого гравця
    def update(self):  
        keys_pressed = key.get_pressed()  
        if keys_pressed [K_s] and self.rect.x > 5 :  
            self.rect.x -= self.speed    

            keys_pressed = key.get_pressed()  
        if keys_pressed [K_w] and self.rect.x < win_width - 80 :  
            self.rect.x += self.speed

# Створення вікна
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Пінг понг")

# Завантажуємо зображення
racket_image = 'racket.png'
ball_image = 'tennis_ball.png'

# Створення спрайтів
racket= Player(racket_image, 5, win_height - 100, 80, 100, 20)
ball= Player(ball_image, 5, win_height - 100, 80, 100, 20)


#Цикл
run = True
clock = time.Clock()

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    keys_pressed = key.get_pressed()


    if keys_pressed[K_DOWN] and racket.rect.y < win_height - 100:
        racket.rect.y += racket.speed

    if keys_pressed[K_UP] and racket.rect.y > 0:
        racket.rect.y -= racket.speed

    # Рух м'ячика
    ball.rect.x += ball.speed
    ball.rect.y += ball.speed

    # Малюємо спрайти
    window.fill((255, 255, 255)) 
    ball.draw(window)

    display.update()
    clock.tick(30) 

time.delay(50)
