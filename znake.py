from pygame import *
from random import *

back = (128,128,128)

window = display.set_mode((700, 700))
display.set_caption('Змейка')



clock = time.Clock()
FPS = 25



speed = 10

game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_y, size_x, player_speed, stepx, stepy):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_y, size_x))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.sx = stepx
        self.sy = stepy

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


            


          
class Player(GameSprite):
    def update(self):
        
        self.rect.y += self.sy
        self.rect.x += self.sx

        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.y > 0:
            self.sx = -10
            self.sy = 0

        if key_pressed[K_d] and self.rect.y < 700  :
            self.sx = 10
            self.sy = 0

        if key_pressed[K_w] and self.rect.x > 0:
            self.sx = 0
            self.sy = -10

        if key_pressed[K_s] and self.rect.x < 700  :
            self.sx = 0
            self.sy = 10
    
class Apple(GameSprite):
    def update(self):
        global lost
        if self.rect.x > 700:
            self.rect.y = randint(0, 700 - 25)
            self.rect.x = randint(0, 700 - 25)
            lost = lost + 1

        
apples = sprite.Group()
for i in range(6):
    apple = Apple('apple.png', randint(0, 700 - 25), randint(0, 700 - 25), 25, 25, 0, 0, 0)
    apples.add(apple)

player = Player('znake.png', 350, 350, 25, 25, 5, 0 , 10)


winer = randint(20, 50)
finish = False


zmeika = []
lost = 0
while game:

    for e in event.get(): 
        if e.type == QUIT:
            game = False


    if finish != True:

        

        font.init()
        font2 = font.SysFont(None, 50)

        window.fill(back)

        player.reset()
        player.update()

        apples.draw(window)
        apples.update()


        new = []
        new.append(player.rect.x)
        new.append(player.rect.y)
        new.append(20)
        new.append(20)
        zmeika.append(new)
        if len(zmeika) > lost:
            del zmeika[0]

        for a in zmeika:
            draw.rect(window, (0, 255, 0), a)
        for a in zmeika[:-1]:
            if a == new:
                finish = True


        collides = sprite.spritecollide(player, apples, True)
        for c in collides:
            lost = lost + 1
            apple = Apple('apple.png', randint(0, 700 - 25), randint(0, 700 - 25), 25, 25, 0, 0, 0)
            apples.add(apple)



        if lost == winer:
            win = font2.render('YOU WIN!!', 100, (255,255,255))
            window.blit(win,(240, 300))
            finish = True      

        if player.rect.x < 0 or player.rect.x > 700 - 20  or player.rect.y < 0 or player.rect.y > 700 - 20  :
            finish = True
            win1 = font2.render('You LOSE!!!', 100, (255,255,255))
            window.blit(win1,(240, 300))

        text = font2.render('Счет: ' + str(lost) + ':' + str(winer), 1, (0,0,0))
        window.blit(text, (0,0))

        
    clock.tick(FPS)
    display.update()