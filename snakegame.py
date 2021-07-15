import pygame
import random
import os
import time


# display size 
width = 400
height = 300

#  display color
white = (255,255,255)
black = (0,0,0)


# pygame initialize
pygame.init()

# create display and store in window variable
window = pygame.display.set_mode((width,height))

# display title
pygame.display.set_caption("i am snake")

# fps
fps = 30
clock = pygame.time.Clock()

# getting system font and storing in font variables
font = pygame.font.SysFont(None,25)


# increaseSnake() function update snake position and increase length of snake after eating food
def increaseSnake(win, color, ls, snake_size):
        for x,y in ls:
            # drawing rectangle to make snake
            pygame.draw.rect(win, color, [x, y ,snake_size, snake_size])


# print score on screen
def textonscreen(text, snake_color, x,y):
    screen_text = font.render(text, True, snake_color)
    window.blit(screen_text, [x,y])


# game function
def firstGame():

    # snake position, size and color
    snake_x_pos = 100
    snake_y_pos = 100
    snake_size = 10
    snake_color = (0,25,0)

    # snake velocity
    initial_velocity = 3
    snake_x_velocity = 0
    snake_y_velocity = 0

    # food postion, size and color
    food_x_pos = random.randint(52,width-10)
    food_y_pos = random.randint(52,height-10)
    food_size = 8
    food_color = (255,0,0)

    # game score
    score = 0

    # snake length and list in which snake position store
    snake_list = []
    snake_length = 1

    # game over conditon
    game_over = False

    if os.path.exists("score.txt") == False:
        with open("score.txt", 'w') as f:
            f.write("0")

    with open("score.txt") as f:
        high_score = f.read()

    while True:
        # after game over if condition true
        if game_over:
            # color the display
            window.fill(white)

            # calling textonscreen function to print game over message
            textonscreen("Game over Press Enter for start Game", snake_color, 40,100)
            textonscreen("Your Score : "+str(score), snake_color, 140,140)

            # open text file for writing high score in file
            if score > int(high_score):
                with open("score.txt",'w') as f:
                    f.write(str(score))

            # pygame.event.get() will return all event which is perform on screen
            for events in pygame.event.get():
                if events.type == pygame.QUIT:      
                    exit()
                if events.type == pygame.KEYUP:     # keyup means when key release
                    if events.key == pygame.K_RETURN:       # K_Return means when enter key press
                        firstGame()     # again calling game function

        else:
            # pygame.event.get() will return all event which is perform on screen
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if events.type == pygame.KEYDOWN:       # keyup means when key press
                    if events.key == pygame.K_RIGHT:
                        snake_x_velocity = initial_velocity     # initialize snake velocity in +ve X direction
                        snake_y_velocity = 0

                    elif events.key == pygame.K_LEFT:
                        snake_x_velocity =  -initial_velocity       # initialize snake velocity in -ve X direction
                        snake_y_velocity = 0

                    elif events.key == pygame.K_UP:
                        snake_y_velocity =  -initial_velocity       # initialize snake velocity in +ve Y direction
                        snake_x_velocity = 0

                    elif events.key == pygame.K_DOWN:
                        snake_y_velocity =  initial_velocity        # initialize snake velocity in -ve Y direction
                        snake_x_velocity = 0
            

            snake_x_pos += snake_x_velocity     # change the snake position in X direction
            snake_y_pos += snake_y_velocity     # change the snake position in Y direction


            # after eating food if condition become true
            if abs(food_x_pos - snake_x_pos)<5 and abs(food_y_pos - snake_y_pos)<5:
                score += 1      #increasing score
                food_x_pos = random.randint(52,width-10)        # changing the food postion in X direction
                food_y_pos = random.randint(52,height-10)       # changing the food postion in Y direction
                initial_velocity += 0.2     # increasing the snake velocity
                snake_length += 2

            # creating list in which snake store
            head = []
            head.append(snake_x_pos)
            head.append(snake_y_pos)
            # append head list in snake_list
            snake_list.append(head)

            # checking if snake_list is greater then snake length then deleting previous position
            if len(snake_list) > snake_length:
                del snake_list[0]

            # if snake fall to the wall then condition become true and game over
            if snake_x_pos > (width-10) or snake_y_pos > (height-10) or snake_x_pos < 1 or snake_y_pos < 51 or head in snake_list[:-1]:
                game_over = True


            # color the display
            window.fill((250,250,250))
    

            # drawing line 
            pygame.draw.line(window, (0,0,0), [0,50],[400,50], 2)

            # drawing rectangle which is known as food
            pygame.draw.rect(window, food_color, [food_x_pos, food_y_pos, food_size, food_size])

            # calling textonscreen() function to print score message 
            textonscreen("Score : "+str(score)+ "    Hight Score : "+high_score, snake_color, 90,20)

            # calling increaseSnake() to updating the postion of snake 
            increaseSnake(window, snake_color, snake_list, snake_size)
        
        # updating screen
        pygame.display.update()
        
        # it control the speed of while loop
        clock.tick(fps)


def startGame():
    
    window.fill(white)

    # loading image and resize and display by blit
    img = pygame.image.load("snake image.jpg")
    img = pygame.transform.scale(img, [width,height+20])
    window.blit(img,[0,0])

    # calling textonscreen() function to print message 
    textonscreen("Welcome to Snake Game Develop By Shanu", black, 20,100)
    textonscreen("Press Space Bar for Start the Game", black, 50,120)

    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()

            if events.type == pygame.KEYUP:
                if events.key == pygame.K_SPACE:
                    firstGame()

        pygame.display.update()
        clock.tick(fps)  


startGame()