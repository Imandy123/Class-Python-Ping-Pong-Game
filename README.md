:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Pong
## CS 110 Final Project
### 1st semester, 2019
### [Assignment Description](https://drive.google.com/open?id=1HLIk-539N9KiAAG1224NWpFyEl4RsPVBwtBZ9KbjicE)

https://github.com/bucs110/final-project-fall19-ping-pong-bois.git

https://docs.google.com/presentation/d/1TWBFFyGNKGuWb6dXQsHYrUvoL0zmub2yzpJmd7VnHyA/edit?usp=sharing

### Team: ping pong bois
#### Andy Liu, Jeffrey Lin, Donal George

***

## Project Description
Our project is a game consisting of a combination between the classic game pong,and ping pong. The user will play against a "AI" we created, and attempts to score point.
***    

## User Interface Design
*  ![gui design](assets/IMG_7225.jpg)
* TBD
# 1. Main Screen
   The main screen allows the user to start the game or check the instructions to play the game.
    ![gui design](assets/menu/frame_000_delay-0.03s.png)
# 2. Game screen
   This is where the actual game takes place when you click on the play button. The ball should bounce off the side of the wall,
   as well as the paddles. If the "AI" misses or hits the net, you gain a point. If the user misses or hits the net, "AI" gains
   the point. When the player beats all the "AI," a congratulation screen will appear. Otherwise, you will be shown the Game Over
   Screen.
   ![gui design](assets/gamebgTBD.png)
# 3. Congratulation screen
   This screen will appear once the user has defeated all the "AI." 
   ![gui design](assets/winning.png)
# 4. Game Over screen
   This screen will appear when the user loses.
   ![gui design](assets/losing.png)
***        

## Program Design
* ![class diagram](assets/class_diagram.jpg)
* Non-Standard libraries
    * pygame
    * For each additional module you should include
        * url for the module documentation
        * a short description of the module
* Class Interface Design
    * TBD
* Classes
    ball- A class that defines the ball- The ball sprite bounces off the sides of the wall, the net, the paddle and will reset when 
    it hits the vertical sides of the screen.
    
    Button- A class that defines the button -When the start button is pressed, moves to gameplay screen. When the instructrions button 
    pressed it will display the instructions necessary to play the game.
    
    Controller- A class that will determine the rules and logic of the game. It also creates the enemy AI.
    
    Net- A class that defines the net- the net will move ranodomly on the middle of the screen.
    
    Paddle- User paddle will move according to the mouse movement, and ball will bounce off the paddle.

***

## Tasks and Responsibilities
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Andy Liu

Makes sure the members are on task, development of movement within the game. Works closely with the Back ENd Specialist to create the code(i.e Ball mechanics, opponement AI). Will work with the Front End Specialist to create the necessary GUI.

### Front End Specialist - Jeffrey
Works on pygame to develop the GUI necessary. Creates the Main Menu Screen, the Play and instructions button Sprite, the ball sprite, the paddle sprite, and finds the music fitting for each GUI. Works with the Back End Specialist so the visualization of the game is consistent.
*most likely pygame

### Back End Specialist - Donal George
Works on coding. Creates the classes necessary for the game to function, such as ball, paddle, net, etc. Works with the Front end Specialist in developing the screens for the game. Works with the Software Lead in creating code for ball mechanics as well as AI movement.
TBD

## Testing
*
    * TBD

* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run Controller()  | 1)Main Screen is Functional 2)Music playing |   
|  2  | click Instructions button  | 1)Music Continues to Play 2) displays necessary instructions needed to play the game 3) music is not affected|               
|  3  | Click escape on keyboard| 1)Goes from the instructions screen to the Main menu 2)goes from the game screen to main menu 3) goes from congratulation/ game over screen to main screen
|  4  | Click Play Button| 1) goes to game screen 2)Main menu music stops, gameplay music starts|
|  5  | Moves Mouse| 1) paddle moves relative to mouse movement 2) when padde comes in contact with ball, ball bounces off paddle|
|  6  | General Playtesting| 1) ball bounces off the side of the screen 2) "oppenent" will move to ball and reflect the ball back 3)once player returns the ball 5 times, speeds up ball 3) if ball hits net or the top/ bottom end of the screen, it counts as a miss |
|  7  | progressing to a win state| 1)If opponement misses, gains a point on the counter 2)When player reaches 11, moves on to new opponement 3)once player beats 5 opponents, players wins
|  8  | progressing to a fail state|  1) if player misses or hits net, opponent gains point. 2) if opponment reaches 11 points before player, player loses|
|  9  | Win state| Displays a congratulation screen
| 10  | fail state| Displays a game over screen
