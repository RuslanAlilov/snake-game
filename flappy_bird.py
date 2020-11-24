import pygame
import random

pygame.mixer.init()

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 1500
screen_height = 1200
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snake Xenzia")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

bgimg = pygame.image.load("/storage/emulated/0/Download/backyy.png")
bgimg = pygame.transform.scale(bgimg, (screen_height,screen_width)).convert_alpha()

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
    
"""def welcome():
	exit_game = False
	while not exit_game:
		gameWindow.fill(white)
		text_screen = font.render("press spacebar to play", black, int(210), int(300))
		text_screen = font.render("press spacebar to play", black,250, 300)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					gameloop()
		pygame.display.update()
		clock.tick(60)"""
						
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# Game Loop
def gameloop():
    pygame.mixer_music.load("/storage/emulated/0/VidMate/download/back.mp3")
    pygame.mixer_music.play()
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 300
    snake_y = 550
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    with open("/storage/emulated/0/high_score.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 2
    snake_size = 30
    fps = 60
    while not exit_game:
        if game_over:
            with open("/storage/emulated/0/high_score.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_2:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_3:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_4:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0,0))
            text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
#welcome()
gameloop()

