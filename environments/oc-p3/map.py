class Map:

    def __init__(self, filename):

        self.filename = filename

    def find_cell_attribute(x,y):
        return current_map[x-1][y-1]

    def open_file(self):
        current_map = []
        
        map_file = open(self.filename,'r')
        for line in map_file:
            current_map.append(line.strip())
        map_file.close()

        print('Map : ',current_map)



ma_map = Map('map-1.txt')

print(ma_map.open_file())