'''
Piet Mondrian was a 20th-century Dutch painter.
He was one of the founders of neoplasticism artistic movement.
'''

import sys, random

try:
    import bext
except ImportError:
    print('This program requires the bext module, wich you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set the constants:
MIN_X_INCREASE = 6
MAX_X_INCREASE = 16
MIN_Y_INCREASE = 3
MAX_Y_INCREASE = 6
WHITE = 'white''
BLACK = 'black'
RED = 'red'
YELLOW = 'yellow'
BLUE = 'blue'


# Setup the screen
width, height = bext.size()
# to print the last column on Windows, we need to add a new line,
# so reduce the width by one:
width -= 1
height -= 3

while True:  # main loop
    # canvas with blank spaces 
    canvas = {}
    for x in range(width):
        for y in range(height):
            canvas[(x, y)] = WHITE

# Generate vertical lines
numberOfSegmentsToDelete = 0
x = random.randint(MIN_X_INCREASE, MAX_X_INCREASE)
while x < width - MIN_X_INCREASE:
    numberOfSegmentsToDelete += 1
    for y in range(height):
        canvas[(x,y)] = BLACK
    x += random.randint(MIN_X_INCREASE, MAX_X_INCREASE)

# Generate horizontal lines:
y = random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)
while y < height - MIN_Y_INCREASE:
    numberOfSegmentsToDelete += 1
    for x in range(width):
        canvas[(x,y)] = BLACK
    y += random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)

numberOfRectanglesToPaint = numberOfSegmentsToDelete - 3
numberOfSegmentsToDelete = int(numberOfSegmentsToDelete * 1.5)

# Select points randomly and try to remove then
for i in range(numberOfSegmentsToDelete):
    while True: # Keep selecting segments to try to delete
        # Get a random start point on an existing segment
        startx = random.randint(1, width - 2)
        starty = random.randint(1, height - 2)
        if canvas[(startx, starty)] == WHITE:
            continue

        # Find out if we're on a vertical or horiontal segment:
        if (canvas[(startx - 1, starty)] == WHITE and 
            canvas[(startx +1, starty)] == WHITE):
            orientation = 'vertical'
        elif (canvas[(startx, starty -1)] == WHITE and
            canvas[(startx, starty +1)] == WHITE):
            orientation = 'horizontal'
        else:
            # The start point is on an intersection,
            # so get a new random start point:
            continue

        pointsToDelete = [(startx, starty)]

        

