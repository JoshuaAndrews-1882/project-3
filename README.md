# Guild Wars

## About

  - This adventure text based game is based on the MMORPG game Guild Wars, which was created by ArenaNet.
  - It has been built using python and text files.

## Project Goals

 - __Usage__

   - This game was primarily built for people who enjoy the game Guild Wars and would like to play for nostalgia reasons
   - People that enjoy adventure story games.
   - In the game there is basic yes and no answer, but also little games to play to complete quests and beat bosses.

 - __Site Owner Goals__

   - I wanted to have a clean game that was easy to read and follow.
   - I wanted to have various elements to the game to keep the player interested.
   - I wanted to stop any invalid entries ruining the game.
   - I wanted a restart function for each quest so they player doesn't have to keep starting over.

 - __Design__

   - Title is yellow as it is a near color to the Guild Wars original title.
   - General text is white as it looks clean and easy to read against a black background.
   - Player score is in green.
   - Enemy score is in red.

 - __Features__

   - Player can enter their name.
![Enter Name](/assets/images/entername.PNG)
   - Some quests require a Y or N answer.
![Yes or No](/assets/images/yn.PNG)
   - Some quests involve mini-games to beat.
![Rock, Paper, Scissors](/assets/images/rps.PNG)
![Number Guess](/assets/images/number.PNG)
![Heads or Tails](/assets/images/headstails.PNG)
![Rll Dice](/assets/images/roll.PNG)
   - Restart quest option if wrong choice is picked or player loses a mini-game.
![Restart Quest](/assets/images/restart.PNG)
   - Restart game if the game is completed.<br>
![Restart Game](/assets/images/complete.PNG)

## Site Design

 - __Flow chart__

![Flow Chart](/assets/images/flowchart.png)

  - The flow chart shows where the player enters their name and then asked if they want to play or not.
  - When a player puts an invalid input it returns to the player input section.
  - If the player fails the quest, they are then asked if they want to restart the quest or not.
  - If the player completes the quest, they move to the next quest.
  - When the player completes the game they are asked if they want to play again or not.
