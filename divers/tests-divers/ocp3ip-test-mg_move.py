from macgyver import MacGyver
from maze import Maze
from position import Position
import settings as constants

instance_maze = Maze(constants.FILENAME) 
instance_macgyver = MacGyver(instance_maze)

mg_pos = instance_macgyver.mg_position
paths = instance_maze.paths
walls = instance_maze.walls

# value = input('une touche ')
value = 'z'

if value == 'z':
    print(f'MG essaye d\'aller vers la droite, à la coordonnée : {Position.up(mg_pos)}')
    if Position.up(mg_pos) in paths:
        new_mg_pos = Position.up(mg_pos)
        print(f'La case est valide, nouvelle position de MacGyver : {new_mg_pos}')
if value == 's':
    print(f'MG essaye d\'aller vers le bas, à la coordonnée : {Position.down(mg_pos)}')
    if Position.down(mg_pos) in paths:
        new_mg_pos = Position.down(mg_pos)
        print(f'La case est valide, nouvelle position de MacGyver : {new_mg_pos}')
if value == 'd':
    print(f'MG essaye d\'aller vers la droite, à la coordonnée : {Position.right(mg_pos)}')
    if Position.right(mg_pos) in paths:
        new_mg_pos = Position.right(mg_pos)
        print(f'La case est valide, nouvelle position de MacGyver : {new_mg_pos}')
if value == 'q':
    print(f'MG essaye d\'aller vers la gauche, à la coordonnée : {Position.left(mg_pos)}')
    if Position.left(mg_pos) in paths:
        new_mg_pos = Position.left(mg_pos)
        print(f'La case est valide, nouvelle position de MacGyver : {new_mg_pos}')