from pygame import* 

class GameSprite(sprite.Sprite):  
  
    def __init__(self, player_image , player_x , player_y, size_x, syze_y, player_speed):  
        sprite.Sprite.__init__(self)  
        self.image = transform.scale(image.load(player_image),(50 , 50))   
        self.speed = player_speed  
        self.rect = self.image.get_rect()  
        self.rect.x = player_x  
        self.rect.y = player_y  
    def reset (self):
        window.blit(self.image,(self.rect.x , self.rect.y))

# Створення руху вверх вниз
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
# Додання картинок


#ігрова сцена  
win_width = 700  
win_height = 500  
window = display.set_mode((win_width, win_height))  
display.set_caption("Пінг понг")  
background = transform.scale

#зображення  
racket = 'racket.png'  
ball = 'tenis_ball.png'

# Спрайти
racket= Player(racket, 5, win_height - 100, 80, 100, 20)
ball= Player(ball, 5, win_height - 100, 80, 100, 20)   

finish = False 

# Цикл гри 
run = True  
  
while run:

        #подія натискання на кнопку Вверх 
      
    for e in event.get():  
        if e.type == QUIT:  
            run = False  

display.update()
time.delay(50)
