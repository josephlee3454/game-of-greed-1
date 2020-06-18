## Game of Greed I

**Authors:** Lee-Roy King, William Koger, Joseph Lee, Roman Sydoruk **Version:** 1.0.0

# Description

Game of Greed I is a python command line version of the dice game. To review rules of game go [here](https://en.wikipedia.org/wiki/Dice_10000)

# Getting Started

* Run command 'python game_of_greed_1.py' in your terminal
* To run the test run 'pytest'

# Architecture

* Python 3.8.3
* Poetry
* Pytest

# Usage 
**GameLogic** - class.\
**calculate score** - static method to GameLogic class with input of a tuple of integers that represent a dice roll.\
**roll_dice** - static method to GameLogic class.\
**Banker** - class.\
**shelf** - instance method with input of the amount of points (integer) to add to shelf.\
**bank** - instance method which can remove all unbanked points.\