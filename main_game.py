import pygame
import random
import os
import time

# Initialize Pygame
pygame.init()

# Define Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
PURPLE = (150, 0, 255)  # Color for reverse power-up

# Game Display Dimensions
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Game Variables
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
reverse_controls = False
reverse_duration = 5  # Duration in seconds for reversed controls
reverse_start_time = None
reverse_powerup_interval = 20  # Power-up appears every 20 seconds
last_reverse_spawn_time = time.time()

# Fonts for game messages
font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 25)

# Global variables for mode selection
DEBUG_MODE = False
ENDLESS_MODE = False

# Functions to display messages
def message(msg, color, y_displace=0, font=None):
    if font is None:
        font = font_style
    mesg = font.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3 + y_displace])

def your_score(score):
    value = score_font.render("Score: " + str(score), True, YELLOW)
    dis.blit(value, [10, 10])  # Positioned with padding from the top-left corner

def display_high_score(score):
    value = score_font.render("High Score: " + str(score), True, YELLOW)
    text_rect = value.get_rect()
    dis.blit(value, [dis_width - text_rect.width - 10, 10])  # Top-right corner padding

# High Score Management Functions
def retrieve_high_score():
    if not os.path.exists("high_score.txt"):
        return 0  # Default high score if file doesn't exist
    with open("high_score.txt", "r") as file:
        return int(file.read().strip())

def save_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))

def update_high_score(score):
    current_high_score = retrieve_high_score()
    if score > current_high_score:
        save_high_score(score)

def mode_selector():
    """
    Displays a start menu to select the mode: Normal, Endless, or Debug with a choice.
    """
    global DEBUG_MODE, ENDLESS_MODE
    while True:
        dis.fill(BLUE)
        message("Select Mode", WHITE, -50)
        message("Press N for Normal Mode", YELLOW, 0)
        message("Press E for Endless Mode", YELLOW, 50)
        message("Press D for Debug Mode", YELLOW, 100)

        # Add legend for colors on the right side
        color_legend_font = pygame.font.SysFont(None, 20)
        dis.blit(color_legend_font.render("Green: Regular Food", True, GREEN), [dis_width - 180, dis_height / 2 - 40])
        dis.blit(color_legend_font.render("Purple: Reverse Controls", True, PURPLE), [dis_width - 180, dis_height / 2])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    DEBUG_MODE = False
                    ENDLESS_MODE = False
                    return
                elif event.key == pygame.K_e:
                    DEBUG_MODE = False
                    ENDLESS_MODE = True
                    return
                elif event.key == pygame.K_d:
                    DEBUG_MODE = True
                    # Prompt for Normal or Endless within Debug Mode
                    dis.fill(BLUE)
                    message("Debug Mode Selected", WHITE, -50)
                    message("Press N for Normal Mode", YELLOW, 0)
                    message("Press E for Endless Mode", YELLOW, 50)
                    pygame.display.update()
                    selecting_debug_mode = True
                    while selecting_debug_mode:
                        for debug_event in pygame.event.get():
                            if debug_event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            elif debug_event.type == pygame.KEYDOWN:
                                if debug_event.key == pygame.K_n:
                                    ENDLESS_MODE = False
                                    selecting_debug_mode = False
                                elif debug_event.key == pygame.K_e:
                                    ENDLESS_MODE = True
                                    selecting_debug_mode = False
                    return

def spawn_item():
    """
    Generates a random position for food or power-up within safe screen boundaries.
    """
    x = round(random.randrange(snake_block, dis_width - snake_block * 2) / snake_block) * snake_block
    y = round(random.randrange(snake_block, dis_height - snake_block * 2) / snake_block) * snake_block
    return x, y

# Main game loop with modes as arguments
def gameLoop():
    global reverse_controls, reverse_start_time, last_reverse_spawn_time

    high_score = retrieve_high_score()  # Get high score at the start
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1

    # Food position generation
    foodx, foody = spawn_item()

    # Reverse power-up initial position (hidden at first)
    reverse_foodx, reverse_foody = None, None

    while not game_over:

        while game_close:
            dis.fill(BLACK)
            message("You Lost!", RED, -30)
            message("Press Q to Quit", YELLOW, 10)
            message("or C to Play Again", YELLOW, 50)
            your_score(Length_of_snake - 1)
            display_high_score(high_score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()  # Restart game without returning to mode selector

        # Check if reverse controls duration has ended
        if reverse_controls and time.time() - reverse_start_time > reverse_duration:
            reverse_controls = False  # End reverse controls

        # Spawn reverse power-up every `reverse_powerup_interval` seconds
        if time.time() - last_reverse_spawn_time > reverse_powerup_interval:
            reverse_foodx, reverse_foody = spawn_item()
            last_reverse_spawn_time = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                # Escape key to exit Endless Mode
                if event.key == pygame.K_ESCAPE and ENDLESS_MODE:
                    print("Exiting Endless Mode")  # Debug print
                    game_over = True
                # WASD controls, reversed if reverse_controls is True
                elif event.key == pygame.K_a and x1_change == 0:
                    x1_change, y1_change = (-snake_block, 0) if not reverse_controls else (snake_block, 0)
                elif event.key == pygame.K_d and x1_change == 0:
                    x1_change, y1_change = (snake_block, 0) if not reverse_controls else (-snake_block, 0)
                elif event.key == pygame.K_w and y1_change == 0:
                    x1_change, y1_change = (0, -snake_block) if not reverse_controls else (0, snake_block)
                elif event.key == pygame.K_s and y1_change == 0:
                    x1_change, y1_change = (0, snake_block) if not reverse_controls else (0, -snake_block)

        # Update snake position and check boundaries
        x1 += x1_change
        y1 += y1_change
        if x1 < 0 or x1 >= dis_width or y1 < 0 or y1 >= dis_height:
            if ENDLESS_MODE:
                Length_of_snake = max(1, Length_of_snake - 3)  # Shrink in endless mode
                x1, y1 = dis_width / 2, dis_height / 2
                snake_List.clear()
            else:
                game_close = True

        dis.fill(BLUE)

        # Display exit message in Endless Mode
        if ENDLESS_MODE:
            exit_message_font = pygame.font.SysFont(None, 20)
            dis.blit(exit_message_font.render("Press ESC to exit Endless Mode", True, YELLOW), [10, dis_height - 30])

        # Draw regular food
        pygame.draw.rect(dis, GREEN, [foodx, foody, snake_block, snake_block])

        # Draw reverse power-up if it's on the screen
        if reverse_foodx is not None and reverse_foody is not None:
            pygame.draw.rect(dis, PURPLE, [reverse_foodx, reverse_foody, snake_block, snake_block])

        # Update snake
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Handle self-collision in Endless Mode
        if snake_Head in snake_List[:-1] and ENDLESS_MODE:
            Length_of_snake = max(1, Length_of_snake - 3)
            snake_List.clear()

        # Draw snake
        for x in snake_List:
            pygame.draw.rect(dis, BLACK, [x[0], x[1], snake_block, snake_block])

        # Display score and high score
        your_score(Length_of_snake - 1)
        display_high_score(high_score)
        pygame.display.update()

        # Check if snake eats regular food
        if x1 == foodx and y1 == foody:
            foodx, foody = spawn_item()
            Length_of_snake += 1

        # Check if snake eats reverse power-up
        if reverse_foodx is not None and reverse_foody is not None and x1 == reverse_foodx and y1 == reverse_foody:
            reverse_controls = True
            reverse_start_time = time.time()  # Start reverse control timer
            reverse_foodx, reverse_foody = None, None  # Hide the reverse power-up until respawn

        clock.tick(snake_speed)

    # Update high score at the end
    update_high_score(Length_of_snake - 1)
    pygame.quit()
    quit()

# Set modes only once and start the game
mode_selector()
gameLoop()  # Start the game in the selected modes
