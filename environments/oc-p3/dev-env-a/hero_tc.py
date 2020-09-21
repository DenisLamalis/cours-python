from map_tc import Map

class Hero:

    def __init__(self, map):
        self.map = map
        self.position = self.map.start
    
    def move(self, direction):
        new_position = getattr(self.position, direction)()
        if new_position in self.map:
            self.position = new_position
    
def main():
    map = Map('map-1.txt')

print(position)


if __name__ == "__main__":
    main()