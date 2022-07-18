# CV Ya Chop

## Demo
### Examples:

| Bot auto-starting the game |
|------------------------------------------------------------------------|
|![Starting the game](https://github.com/SarthakHa/CV_Ya_Chop/blob/main/gifs/Kick_Start.gif)| 

| Bot playing the game |
|------------------------------------------------------------------------|
|![Playing Game](https://github.com/SarthakHa/CV_Ya_Chop/blob/main/gifs/Kick_Game.gif)| 


## Getting Started
To run the program,

1. Open a tab in your browser to the link https://www.addictinggames.com/clicker/kick-ya-chop
2. Run program with command from base of repo
   ```
   python3 src/main.py --runs=10
   ```
   The runs is the number of kicks the program should run for
3. Switch your screen to the browser tab with the game.
4. Watch it play! If you need to exit, go back to cli where program was ran and use `ctrl+c`

## About the project
There are some tests included in the project, they can be run by
```
python3 -m pytest
```
or
```
pytest
```

## Performance
Best score achieved = 139

## Possible future improvements
A delay is required to get the program to function. This is because when a wood block is kicked, a kicked off block animation runs. this blocks some of the detection and can lead to an erenous templateMatching output. There are potential ways to optimize so that this animation is not an issue.