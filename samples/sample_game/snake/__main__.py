from .game import init, deinit, loop

if __name__ == "__main__":
    # Initialize the game
    state, graphics = init()
    # Run the game loop
    loop(state, graphics)
    # Close window
    deinit()

