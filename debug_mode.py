# debug_mode.py

import logging

# Set up the logging configuration
logging.basicConfig(filename="game_debug.log", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def log_debug_info(snake_list, food_position, score, direction, speed):
    """
    Logs the game state for debugging purposes.
    
    Args:
    - snake_list: List of coordinates representing the snake's body.
    - food_position: Tuple of x, y coordinates for the food.
    - score: Current score of the game.
    - direction: Current direction of the snake.
    - speed: Current speed of the snake.
    """
    logging.debug(f"Snake Position: {snake_list}")
    logging.debug(f"Food Position: {food_position}")
    logging.debug(f"Score: {score}")
    logging.debug(f"Direction: {direction}")
    logging.debug(f"Speed: {speed}")
