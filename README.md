# Vegeta's Nighmare
Vegeta's Nightmare Game in Python using Pygame.
<p align="center">
  <img src="https://github.com/baez97/Nightmare/blob/master/images/Screenshot.png"/>
</p>

## Objective of the game
The object of the game is to kill al the enemies (cells) before dying, but they are enclosed so you can't attack them until you get the SuperSaiyan State that allows you to shoot energy balls.

## Controls
The actions you can do are:

| Action | Keys |
| ------ | :---: |
| Move up, down, left and right | `Arrow Keys`|
| Attack right | `D` |
| Attack left  | `A` |
| Pick up an item | `E` | 
| Open a Hole | `E` |
| Get into a Hole | `E` |

## Obtaining the SuperSaiyan State
In order to obtain the SuperSaiyan state you must collect the three fire medals (Red, Blue and Gold). Once you get the third one, Vegeta is automatically powering up. This state suppose that Vegeta moves faster and he is able to shoot Energy Balls.
<p align="center">
  <img src="https://github.com/baez97/Nightmare/blob/master/images/vegetaPU/poweringUp.gif"/>
</p>

> During the powering up animation, the display will turn darker and the game will be stopped until the animation is completed.
## Energy Balls
Energy balls are shot by the enemies and by vegeta (SuperSaiyan). They kill the enemies at one hit, and they cause a damage of one life in Vegeta. They are not stopped by the obstacles, only by the walls (borders of the game).
<p align="center">
  <img src="https://github.com/baez97/Nightmare/blob/master/images/ball/ball_right.png"/>
</p>

## Holes
The maze shows some holes in the floor, some of them are closed with a lock. In order to open them you need to obtain a key that once it is used, it cannot be used anymore (you will need to obtain another one in order to open other hole).
In order to get into the hole, you just put vegeta in the proper cell and press `E`. 
<p align="center">
  <img src="https://github.com/baez97/Nightmare/blob/master/images/Hole.png"/>
</p>

> If the hole was locked and you had a key, it will be unlocked and you will have to press `E`again in order to get into it.

## Obstacles
They avoid you to go through it, but they do not stop energy balls. In order to go to an area sepparated of yours by obstacles, you can use the holes.
<p align="center">
  <img src="https://github.com/baez97/Nightmare/blob/master/images/GrassTile.png"/>
</p>

## Enemies
The enemies are static and they shoot energy balls in a constant frecuency. If the character is hit by an energy ball, its life will be reduced in one heart.

<p align="center">
  <img src="https://github.com/baez97/Nightmare/blob/master/images/Cell/r_3.png"/>
</p>

> At the beginning, the character is able to attack by kicking, but the enemies are sepparated from the character by walls. The only way to kill them is by shooting energy balls to them when SuperSaiyan State is achieved.


# Design patterns 
| Pattern | Description |
| --- | --- |
| Decorator | The tiles of the maze are decorated with the items that are above them (key, hole, heart) and they extend the functionality of the tile allowing vegecta to interact with it. |
| State | The character, the enemies and the item's behaviour depends on its state (moving up, stopped, obtained) |
| Bidimensional State | The character has the basic states (movingUp, stopped...) but also a super state (SuperSaiyan or normal). The combination of all states is implemented applying the state pattern again over the super state, so the character only has a super state, and the super state has a basic state, given the fact that the behaviour of the basic states depends also on the super state (the character moves faster if its super state is SuperSaiyan) |
| Visitor | Some functionalities of the character depends on the items of the bag. For example, hasKey() goes through all the elements of the bag asking if it is a key, only the key returns True. |
| Flyweight | Energy balls are movable objets, so they have a state also. Instead of creating a new instance of state for each ball, all of them share the states through a flyweight class implemented in the Factory |
| Mediator | The movable objects does not know each other, so for controlling colissions they ask the game for the element in that position through a Colission Manager class |
| Factory Method | All the instances (except from Game and Factory) are created in the Factory class. This class is used also as the Sprite manager (all the images are loaded here)|
| Template | Maze class has a method `PaintAll()` that defines the skeleton of the algorithm, but leaves other classes to implement the behaviour. For example by making the call to `self.paintCharacter()` that calls `game.paintCharacter()`, leaving that game paints the Character, but following the order of the skeleton defined.|
| Observer | Game is the only class with access to the GUI display, and it calls all the elements that must be painted for them to tell him which image and where should be painted (position).|
| Proxy | The HoleDecorator has a link to another maze, but in order to make it more efficient, it only stores the string of the dictionaire that corresponds. For example, "underground", so the other maze will be loaded under demand.|
| Iterator | All the methods of the Bag and MedalBox classes goes through all their sons, iterating the `sons`collection |
| Bridge | The way that State has been implemented in `movableObject` suppose a separation between the abstraction of a `movableObject` and its implementation (`state`)|
