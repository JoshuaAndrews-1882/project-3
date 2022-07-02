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

## Bugs

- __Fixed__

  - With restarting quest if a player entered anything other than Y or N it would restart the game.  Required another While True.
  - Old text would stay on the terminal when restarting the game, required additional os.system('clear') after the question was asked to remove it.
  - For Elona if a player entered a letter it would respond with too high or too low, it required try/except ValueError for when a player entered non-numerical.

- __Not Fixed__

  - Unaware of any other bugs.

## Future Features

- Player lives so they game restart if a player restarts a quest x amount of times.
- New quests to different locations.
- Record what locations the player has fully completed.
- Add more quests to give the story more depth.
- Add a player class/weapon system so the story is more personalized.

## Testing

- __Validator Testing__

 - Validated code through PEP8 Online.
![PEP8](/assets/images/PEP8.PNG)

## Technologies Used

 - Python
 - Python Libraries
  - random
  - os
 - GitHub
  - Version control
 - GitPod
  - Developlent Tool
 - Heroku
  - Deploy code in a terminal
 - PIP8 Online
  - Validate Python code
 - Lucid
  - Create game flow chart


## Deployment

- __GitHub and GitPod:__

  - Create new repository from the Code Institute Python template.
  - Create workspace in GitPod.
  - Add, commit and push changes made on GitPod to GitHub.

- __Heroku__

 - Create a new app in Heroku.
 - Name the app, select region and then click create app.
 - In Settings click Config VARS and set Key as PORT and Value as 8000.
 - Add Buildpack, heroku/python and heroku/nodejs.  Ensure it is the correct order as written.
 - In Deploy section, select GitHub and connect.
 - Search for GitHub repository name and press connect to link Heroku to GitHub.
 - Enable Automatic Deploys so Heroku automatically updates when pushing a new change to code to GitHub.
 - Click view to look.
 - When logging in to Heroku, click Open app in top right of the banner to view the terminal.