import pygame
import time
from pygame.locals import *
import random

SIZE = 40
BACKGROUND_COLOUR = (110, 59, 202)
class Apple:
    def __init__(self,parent_screen):
        self.fruit = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen=parent_screen
        self.x = 120
        self.y = 120

    def draw(self):
        #self.parent_screen.fill((110, 59, 202))  # to remove the previous images
        self.parent_screen.blit(self.fruit, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE

class Snake:
    def __init__(self,parent_screen,length):

        self.parent_screen = parent_screen
        #self.python = pygame.image.load("resources/pythonhead1.jpg").convert()
        self.direction = "right"

        self.length = length
        self.x=[40]*length
        self.y=[40]*length


    def move_left(self):
        self.direction = "left"
        #self.draw()

    def move_right(self):
        self.direction = "right"
        #self.draw()

    def move_up(self):
        self.direction = "up"
        #self.draw()

    def move_down(self):
        self.direction = "down"
        #self.draw()
    def walk(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]



        if self.direction == "left":
            self.x[0] -= SIZE
        if self.direction == "right":
            self.x[0] += SIZE
        if self.direction == "up":
            self.y[0] -= SIZE
        if self.direction == "down":
            self.y[0] += SIZE
        self.draw()

    def draw(self):
        self.parent_screen.fill(BACKGROUND_COLOUR)  # to remove the previous images

        for i in range(self.length):
            self.parent_screen.blit(self.python, (self.x[i], self.y[i]))
        pygame.display.flip()
        # time.sleep(5)   #how long the window lasts
    def increase_length(self):
        self.length +=1
        self.x.append(-1)
        self.y.append(-1)

class Black_Snake(Snake):
    def __init__(self,parent_screen,length):
        super().__init__(parent_screen,length)
        self.python = pygame.image.load("resources/blackhead.jpg").convert()
class Green_Snake(Snake):
    def __init__(self,parent_screen,length):
        super().__init__(parent_screen,length)
        self.python = pygame.image.load("resources/pythonhead1.jpg").convert()
class Red_Snake(Snake):
    def __init__(self,parent_screen,length):
        super().__init__(parent_screen,length)
        self.python = pygame.image.load("resources/redblock.jpg").convert()



class Game:


    def __init__(self):
        pygame.init()  # initialize window
        self.surface = pygame.display.set_mode((1000,800))  # dimensions of the window
        snakes = [Black_Snake, Green_Snake,Red_Snake]
        the_chosen_one = random.choice(snakes)
        self.snake = the_chosen_one(self.surface,1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True

        return False

    def is_outside_screen(self,x,x1,y,y1):
        if x1 not in range(0,x) or y1 not in range(0,y):
            return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score:{self.snake.length}",True,(200,200,200))
        self.surface.blit(score,(850,10))

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        #snake colliding with apple
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.apple.move()
            self.snake.increase_length()
            #print("collision")
        #snake colliding with itself
        for i in range(1,self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                raise("Game Over")
        #snake leaves the screen
        if self.is_outside_screen(1000,self.snake.x[0],800,self.snake.y[0]):
            raise ("Game Over")

    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOUR)
        font = pygame.font.SysFont('arial', 35)
        line1 = font.render(f"Score:{self.snake.length}",True,(200,200,200))
        self.surface.blit(line1,(100,300))
        line2 = font.render(f"To play again press Enter,To exit press Escape!", True, (200, 200, 200))
        self.surface.blit(line2,(100,350))
        pygame.display.flip()
    def reset(self):
        snakes = [Black_Snake, Green_Snake, Red_Snake]
        the_chosen_one = random.choice(snakes)
        self.snake = the_chosen_one(self.surface, 1)
        self.apple = Apple(self.surface)
    def run(self):

        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pause = False
                        self.reset()
                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
            time.sleep(0.05+(0.5/self.snake.length))#time delay between movement



if __name__ == "__main__":
    game = Game()
    game.run()










