Things to Do
============

This is a very simple To-Do list.
You can mark a task as done by changing a line to `[X]`.

Simple Tasks 
------------

These tasks require close to zero python knowledge.

 - [ ] Change the color of the snake by modifying the variables `head_color`
       and `body_color` of the class `GraphicState`

 - [ ] Upgrade your game to 60 FPS by changing the variable `GraphicsState.fps`

 - [ ] Change the font of the game over text

 - [ ] Change the grid size of the game 
    - [ ] Modifying the variable `grid_size` of the class `GameState`.
    - [ ] Update `GraphicState.cell_size` or `GraphicState.offset_x` and
          `GraphicState.offset_y` accordingly

Intermediate Tasks
------------------

The goal here is to learn Git, not Python, but if you need to wait a lot, here
are other simple tasks:

 - [ ] In game over implement reset function to play again when a key (or any
       key) is pressed.

 - [ ] Add logic to let player win: if the player reaches the score of
       `grid_size * grid_size - 1`, the game is won (snake fills the entire
       board).

 - [ ] Add pause feature: when the player presses a key, the game pauses until
       the same key is pressed again. You can add a new variable `GameState.paused`
       to keep track of this.

 - [ ] Make the game harder:
    - [ ] Make game go faster every 10 points in `GameState.score`, by
          decreasing `GameState.tick`
    - [ ] If the player does not eat the food in 500 ticks, progressively
          decrease the grid size (eg by 1 every 100 ticks). When the player
          eats the food grid is restored to original size.

 - [ ] Use a cool retro font
    - [ ] Download the UNSCII font from http://viznut.fi/unscii/
    - [ ] Load font in PyGame and use it to change the game over text

 - [ ] Fix rendering bug of snake when game over

 - [ ] Fix bug by checking that the new food does not overlap with the snake

 - [ ] Add a text on startup that says "Welcome to snake, press any key to start"


Long(er) Tasks
--------------

Are you bored? Do the Git tutorial first!

 - [ ] Improve rendering of snake by adding more details

 - [ ] Add a menu screen

 - [ ] Implement a scoreboard
    - [ ] Create a scoreboard screen
    - [ ] Let players enter their name
    - [ ] Create a system to store past scores

