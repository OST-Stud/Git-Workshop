"""
Simple Game of Snake
====================

This code is for the participants of the Git Workshop at the Ostschweizer
Fachhochschule in Rapperswil. The code is provided without any warranty.
"""

import random
import pygame


class GameState:
    """ Store all information related to the game logic """
    tick_length: float = (1e3 / 8)      # 1 / UPS, speed of the game, in milliseconds
    since_last_tick: float = 0          # Time since last tick
    running: bool = True                # Game is running
    game_over: bool = False             # Game is over
    score: int = 0                      # Score of the player
    grid_size: int = 21                 # Grid size of game
    direction: tuple[int, int] = (0, 0) # Direction of the snake
    head: tuple[int, int] = (10, 10)    # Coordinates for snake head
    body: list[tuple[int, int]] = []    # Coordinates of body
    food: tuple[int, int] = (0, 0)      # Coordinate of food


class GraphicState:
    """ Store all information related to graphics (rendering) """
    screen: pygame.Surface # Surface to render on
    fps: int       = 30    # Frames per second
    cell_size: int = 30    # Size of cells
    window_h: int  = 600   # Height of the window, default must match cell_size * grid_size
    window_w: int  = 600   # Width of the window, default must match cell_size * grid_size
    offset_x: int  = 0     # Offset for x axis
    offset_y: int  = 0     # Offset for y axis
    bg_color:   tuple[int, int, int] = (255, 255, 255) # Color of background
    grid_color: tuple[int, int, int] = (200, 200, 200) # Color of grid
    text_color: tuple[int, int, int] = (200,  50,  20) # Color of text
    food_color: tuple[int, int, int] = (200, 200,  20) # Color of food
    head_color: tuple[int, int, int] = (200,  50,  20) # Color of snake head
    body_color: tuple[int, int, int] = (  0, 200, 100) # Color of snake body


def init() -> tuple[GameState, GraphicState]:
    """ Initialize the game. """
    # Initialize pygame and create window
    pygame.init()

    # Set window title
    pygame.display.set_caption("OST FH Git Workshop - Snake")
    
    # Create game state
    state = GameState()
    graphics = GraphicState()

    # Initialize random food location
    state.food = (random.randint(0, state.grid_size - 1),
                  random.randint(0, state.grid_size - 1))

    # Create pygame screen
    graphics.screen = pygame.display.set_mode((state.grid_size * graphics.cell_size,
                                               state.grid_size * graphics.cell_size),
                                              pygame.RESIZABLE)

    return state, graphics


def deinit():
    """ Deinitialize the game. """
    pygame.display.quit()
    pygame.quit()


def loop(state: GameState, graphics: GraphicState) -> tuple[GameState, GraphicState]:
    """ Run the game loop. """

    # Clock to keep track of FPS and game ticks
    clock = pygame.time.Clock()

    # Game loop
    while state.running:
        # Handle external events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.running = False

            # Handle arrows or WASD to change direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if state.direction != (0, 1):
                        state.direction = (0, -1)

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if state.direction != (0, -1):
                        state.direction = (0, 1)

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if state.direction != (1, 0):
                        state.direction = (-1, 0)

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if state.direction != (-1, 0):
                        state.direction = (1, 0)

            # Handle window resize event
            if event.type == pygame.VIDEORESIZE:
                # Update window size
                graphics.window_h = event.h
                graphics.window_w = event.w

                # Compute new cell size based on window size, take smaller value between width and height
                graphics.cell_size = min(graphics.window_w, graphics.window_h) // state.grid_size

                # Offset to center grid and other things in window
                graphics.offset_x = (graphics.window_w - state.grid_size * graphics.cell_size) // 2
                graphics.offset_y = (graphics.window_h - state.grid_size * graphics.cell_size) // 2

        # ╻ ╻┏━┓╺┳┓┏━┓╺┳╸┏━╸
        # ┃ ┃┣━┛ ┃┃┣━┫ ┃ ┣╸ 
        # ┗━┛╹  ╺┻┛╹ ╹ ╹ ┗━╸

        # Update game if enough time has passed
        if state.since_last_tick >= state.tick_length and not state.game_over:
            # Update counter
            state.since_last_tick = 0

            # Game over if snake crosses itself
            if state.head in state.body:
                state.game_over = True

            else:
                state.body.append(state.head)

                # Grow snake if over food
                if not state.head == state.food:
                    state.body.pop(0)

                else:
                    state.score += 1

            # Generate new food
            if state.head == state.food:
                state.food = (random.randint(0, state.grid_size - 1),
                              random.randint(0, state.grid_size - 1))

            # Update snake head
            state.head = ((state.head[0] + state.direction[0]) % state.grid_size,
                          (state.head[1] + state.direction[1]) % state.grid_size)
 
        # ┏━┓┏━╸┏┓╻╺┳┓┏━╸┏━┓╻┏┓╻┏━╸
        # ┣┳┛┣╸ ┃┗┫ ┃┃┣╸ ┣┳┛┃┃┗┫┃╺┓
        # ╹┗╸┗━╸╹ ╹╺┻┛┗━╸╹┗╸╹╹ ╹┗━┛

        # Clear screen
        graphics.screen.fill((0, 0, 0))

        # Render cells
        for y in range(state.grid_size):
            for x in range(state.grid_size):

                # Draw cell, inside white
                pygame.draw.rect(graphics.screen, graphics.bg_color,
                                (graphics.offset_x + x * graphics.cell_size,
                                 graphics.offset_y + y * graphics.cell_size,
                                 graphics.cell_size, graphics.cell_size))

                # Draw cell borders, gray
                pygame.draw.rect(graphics.screen, graphics.grid_color,
                                (graphics.offset_x + x * graphics.cell_size,
                                 graphics.offset_y + y * graphics.cell_size,
                                 graphics.cell_size, graphics.cell_size), 1)

        # Draw food
        pygame.draw.rect(graphics.screen, graphics.food_color,
                         (graphics.offset_x + state.food[0] * graphics.cell_size,
                          graphics.offset_y + state.food[1] * graphics.cell_size,
                          graphics.cell_size, graphics.cell_size))

        # Draw snake head
        pygame.draw.rect(graphics.screen, graphics.head_color,
                         (graphics.offset_x + state.head[0] * graphics.cell_size,
                          graphics.offset_y + state.head[1] * graphics.cell_size,
                          graphics.cell_size, graphics.cell_size))

        # Draw snake body
        for (body_x, body_y) in state.body:
            pygame.draw.rect(graphics.screen, graphics.body_color,
                            (graphics.offset_x + body_x * graphics.cell_size,
                             graphics.offset_y + body_y * graphics.cell_size,
                             graphics.cell_size, graphics.cell_size))

        if state.game_over:
            # Draw game over
            font = pygame.font.SysFont("Arial", 30, bold = True)
            text = font.render("Game Over", True, graphics.text_color)
            graphics.screen.blit(text, (graphics.window_w // 2 - text.get_width() // 2,
                                        graphics.window_h // 2 - text.get_height() // 2))

            # Draw score
            font = pygame.font.SysFont("Arial", 30)
            text = font.render(f"Score: {state.score}", True, graphics.text_color)
            graphics.screen.blit(text, (10, 10))

        # Draw screen
        pygame.display.flip()

        # Keep 60 FPS framerate
        dt = clock.tick(graphics.fps)
        state.since_last_tick += dt

    return state, graphics
