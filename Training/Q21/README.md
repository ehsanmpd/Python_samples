# Question
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
- UP 5
- DOWN 3
- LEFT 3
- RIGHT 2


The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.


# Sample output
Type direction step (to terminate type 0):DOWN 1

Current position:  [0, -1]

Type direction step (to terminate type 0):UP 5

Current position:  [0, 4]

Type direction step (to terminate type 0):LEFT 1

Current position:  [-1, 4]

Type direction step (to terminate type 0):RIGHT 10

Current position:  [9, 4]

Type direction step (to terminate type 0):UP 2

Current position:  [9, 6]

Type direction step (to terminate type 0):LEFT 3

Current position:  [6, 6]

Type direction step (to terminate type 0):0

Distance:  8
