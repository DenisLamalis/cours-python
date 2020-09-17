class Map:

    def __init__(self, filename):
        
        current_map = []

        map_file = open(filename,'r')
        for line in map_file:
            current_map.append(line.strip())
        map_file.close()

    def find_cell_attribute(x,y):
        return current_map[x-1][y-1]


ma_map = Map('map-1.txt')

print(ma_map)