# Hannahs_Snake_Game
Welcome to my version of the popular Snake Game!
# Rules
The same rules of Snake still apply. 
- The goal of the game is to collide the snake's head with the blue circle, of which is the food.
- Use the up, down, right, left keys on your keyboard to move the snake. 
- Don't allow the snake's head to hit the boundaries of the wall, otherwise the snake will reset it's position to the origin. 
- Don't allow the snake's head to hit another segment of it's body, while making a turn.
- You are unable to move the snake's head to the left, if the body is currently moving to the right. 
  - The same goes for the up and down key. 
- If the snake's head gets within a certain distance of the blue circle, you will receive a point added to your score, and the blue circle will reset to a different random position. 
- The length of the snake will also increase with each point that you get.
- If once you die, you get a score higher than the highest score saved in a separate file called highscore.txt, your new high score will replace the highest score saved in the txt file. 
# Breakdown of Game Creation
- I used Object Oriented Programming(OOP) to create this snake game, as there are multiple different objects, with their own set of attributes and functionality.
- I created different classes for the snake object itself, the scoreboard, and the food. 
  - This was essential, as I wanted to be able to manipulate and handle all objects separately.
- I imported the turtle module to create the graphics, visuals, and screen object. 
- I also used the time module to delay the graphics, such that the snake head and body appeared to be one, complete object, rather than individual pieces.
# Concepts 
- This project was monumental for me, as it strengthed my understanding of OOP, and helped smooth the transition from procedural programming to OOP.
- Class Inheritance: Inheriting functionality from the Turtle class into classes I was creating.

# Conclusion
Overall, I had a blast working on this project. To anyone who has a comment, or advice, please let me know! I always appreciate constructive criticism. Have fun with Snake!



