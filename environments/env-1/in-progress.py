
# create the map

current_map = []

map_file = open('map.txt','r')

for line in map_file:
    current_map.append(line.strip().split(','))

map_file.close()

print(current_map)