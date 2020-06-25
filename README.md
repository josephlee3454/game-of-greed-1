## Game of Greed I

**Authors:** Lee-Roy King, William Koger, Joseph Lee, Roman Sydoruk 
**Version:** 1.0.0

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



# overveiw of tasks
* Application should implement all features from previous version
* Application should simulate rolling between 1 and 6 dice
* Application should allow user to set aside dice each roll
* Application should allow “banking” current score or rolling again.
* Application should keep track of total score
* Application should keep track of current round
* Application should have automated tests to ensure proper operation

User Acceptance Tests
Convert required features into suite of passing unit tests
E.g. test_roll
doing a roll with x number of dice should return sequence of x length random integers between 1 and 6 inclusive
Use an automated tool to ensure correct behavior from end user’s perspective



Feature Tasks and Requirements
Application should implement features from versions 1 and 2
Should handle when cheating occurs.
Or just typos.
E.g. roll = [1,3,5,2] and user selects 1, 1, 1, 1, 1, 1
Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.
Handle zilch
No points for round, and round is over
Any other questions refer to game doc or the online game or ask.

User Acceptance Tests
Must pass provided unit and flow tests.