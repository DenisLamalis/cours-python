from draw_maze import MazeScreen

instance_screen = MazeScreen()

m = Maze(constants.FILENAME)  
ms = MazeScreen(m.paths, m.walls, m.start, m.goal, m.items)
ms.draw_maze()