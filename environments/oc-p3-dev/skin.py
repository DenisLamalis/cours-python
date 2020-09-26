
class Skin:
    """ I'm the object who give a skin. """
    def __init__(self):
        pass

    def image(self, type):
        if type == 'path':
            return 'images/floor.bmp'
        elif type == 'wall':
            return 'images/wall.bmp'
        elif type == 'start':
            return 'images/MacGyver.png'
        elif type == 'goal':
            return 'images/Gardien.png'
        elif type == 'player':
            return 'images/MacGyver.png'
