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



# Overview
* Today you’ll begin working in teams on a command line version of the dice game Game of Greed by expanding your understanding of Python standard library.

* Feature Tasks and Requirements
* Today is all about tackling the highest risk and/or highest priority features - scoring, dice rolling and banking of points.
* Define a GameLogic class.
* Handle calculating score for dice roll
* Add calculate_score static method to GameLogic class.
* The input to calculate_score is a tuple of integers that represent a dice roll.
* The output from calculate_score is an integer representing the roll’s score according to rules of game.
* Handle rolling dice
* Add roll_dice static method to GameLogic class.
* The input to roll_dice is an integer between 1 and 6.
* The output of roll_dice is a tuple with random values between 1 and 6.
* The length of tuple must match the argument given to roll_dice method.
**********************************************
* Handle banking points
* Define a Banker class
* Add a shelf instance method
* Input to shelf is the amount of points (integer) to add to shelf.
* shelf should temporarily store unbanked points.
* Add a bank instance method
* bank should add any points on the shelf to total and reset shelf to 0.
* bank output should be the amount of points added to total from shelf.
* Add a clear_shelf instance method
* clear_shelf should remove all unbanked points.* 
