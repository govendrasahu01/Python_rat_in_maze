Rat in Maze - README


Overview

The "Rat in Maze" project is a Python program that simulates a maze-solving scenario where a rat navigates through a maze from the starting point (S) to the endpoint (E). The maze is randomly generated with obstacles represented by "▒" and open paths represented by "◌". The rat's movements are displayed on the console, and the program provides options to solve the maze and print the path or generate a new maze.

Features 

Maze Generation:

    The maze is randomly generated with a specified size (n x n).
    Obstacles are placed in the maze with a probability of 25% at each position.
    The starting point (S) is set at the top-left corner, and the endpoint (E) is set at the bottom-right corner.

Maze Display:

    The maze is displayed on the console using ASCII characters.
    Obstacles are displayed in yellow ("▒"), open paths in blue ("◌"), the starting point in white ("S"), and the endpoint in white ("E").
    The maze borders are displayed in red.
    
Maze Solving:

    The program provides two methods for solving the maze:
    Single Solution: Finds a single path from the starting point to the endpoint.
    All Solutions: Finds all possible paths from the starting point to the endpoint.
    The rat's path is marked with "☻" in the solved maze.

User Interaction:

    The user is prompted to choose between generating a new maze, solving the maze, or exiting the program.
    Input validation is implemented to ensure the user enters a valid choice and maze size.


How to Run the Program

    Ensure you have Python installed on your system.
    Save the provided code in a file with a ".py" extension, for example, "rat_in_maze.py".
    Open a terminal or command prompt and navigate to the directory containing the file.
    Run the program using the command: python rat_in_maze.py


Instructions

Generating a Maze:

    Choose option 2 to generate a new maze.
    Enter the desired maze size (between 3 and 15).

Solving the Maze:

    Choose option 1 to solve the maze.
    The program will attempt to find a path from the starting point to the endpoint.
    If a solution is found, the solved maze will be displayed.
    If no solution is found, a message indicating that the rat can't cross the maze will be displayed.

Menu Options:

    After generating or solving a maze, the program provides menu options:
    Option 1: Print the path in the solved maze.
    Option 2: Generate another maze.
    Option 3: Exit the game.

Exiting the Program:

    Choose option 3 to exit the program.

Note

    The program uses ANSI escape codes to colorize console output. Ensure that your terminal supports ANSI escape codes for the best visual experience.
    The maze generation and solving algorithms are implemented using recursive techniques.


Feel free to explore and enjoy the Rat in Maze simulation!

readme.md credit - chat.openai.com
