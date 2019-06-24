from draw import Maze
import time

"""
# Smaller maze
"""
maze_data = ( ( 2, 0, 1, 0, 0 ),
              ( 0, 0, 0, 0, 1 ),
              ( 1, 1, 1, 0, 0 ),
              ( 1, 0, 0, 0, 0 ),
              ( 0, 0, 2, 0, 1 ))


# 0 - empty square
# 1 - occupied square
# 2 - occupied square with a beacon at each corner, detectable by the robot

# maze_data = ( ( 1, 1, 0, 0, 2, 0, 0, 0, 0, 1 ),
#               ( 1, 2, 0, 0, 1, 1, 0, 0, 0, 0 ),
#               ( 0, 1, 1, 0, 0, 0, 0, 1, 0, 1 ),
#               ( 0, 0, 0, 0, 1, 0, 0, 1, 1, 2 ),
#               ( 1, 1, 0, 1, 1, 2, 0, 0, 1, 0 ),
#               ( 1, 1, 1, 0, 1, 1, 1, 0, 2, 0 ),
#               ( 2, 0, 0, 0, 0, 0, 0, 0, 0, 0 ),
#               ( 1, 2, 0, 1, 1, 1, 1, 0, 0, 0 ),
#               ( 0, 0, 0, 0, 1, 0, 0, 0, 1, 0 ),
#               ( 0, 0, 1, 0, 0, 2, 1, 1, 1, 0 ))

world = Maze(maze_data)
world.draw()

while True:
    time.sleep(1000)