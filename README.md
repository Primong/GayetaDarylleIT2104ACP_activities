# Spartan Shuttlers: Badminton Players Management System

Badminton Player Management System is a program that allow users to manage player information through various functionalities such as adding, viewing, searching, updating, and deleting player details. 

# Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#https://github.com/Primong/GayetaDarylleIT2104ACP_activities/edit/main/README.md#data-structures)
3. [Explanation of how Python concepts, libraries, etc. were applied](#Explanation-of-how-Python-concepts,-libraries,-etc.-were-applied)
   - [Object-Oriented Programming (OOP)](#object-oriented-programming-(oop))
   - [Data Structures](#data-structures)
   - [Input Validation](#input-validation)
   - [Methods and Functions](#methods-and-functions)
   - [String Manipulation](#string-manipulation)
   - [Control Flow](#control-flow)
   - [Gender Statistics](#gender-statistics)
   - [Error Handling](#error-handling)
   - [Main Program Execution](#main-program-execution)
4. [Details of the chosen SDG and its integration into the project](#details-of-the-chosen-sdg-and-its-integration-into-the-project)

# l. Project Overview
The Badminton Player Management System is a console-based application designed to help manage and maintain a list of badminton players. This system allows administrators to add, view, update, delete, and search for players based on unique identifiers. It also includes a feature to display gender statistics, showing the number of male and female players in the system. The system is designed to be user-friendly, offering a simple menu interface to perform various actions related to player data management.

# ll. Features
Add a Player

View All Players

Search for a Player

Update Player Information

Delete a Player

Display Gender Statistics

Exit the System

# lll. Explanation of how Python concepts, libraries, etc. were applied
### Object-Oriented Programming (OOP)
1.1 The system utilizes two classes: Player and BadmintonPlayerManagementSystem. OOP principles like encapsulation were applied.

1.2 Encapsulation: The player data is encapsulated inside the Player object, and the system is responsible for managing multiple players.

### Data Structures
2.1 Lists: The player information is stored in a list (self.players), where each element is an instance of the Player class. This allows dynamic management and retrieval of player data.

### Input Validation
3.1 Input Handling and Validation: The system handles user input through the input() function and performs validation to ensure that the inputs for age, rank, and gender are valid. This is done using try-except blocks to catch invalid values (e.g., non-integer values for age or rank).

3.2 While Loops: These are used to repeatedly ask the user for input until valid data is entered. This ensures that the system is robust and prevents invalid data entry.

### Methods and Functions
4.1 Methods: Functions are defined as methods inside the classes to carry out specific tasks like adding a player (add_player()), viewing players (view_players()), searching for a player (search_player()), and updating player details (update_player()).

### String Manipulation
5.1 String Formatting: Python's string formatting (f"...") is used to generate readable and user-friendly output when displaying player details. This helps present player information in a clear, readable format.
