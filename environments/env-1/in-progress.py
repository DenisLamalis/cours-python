
# create the map

current_map = []
current_map2 = []

# map_file = open('map-1.txt','r')

# for line in map_file:
#     current_map.append(line.strip().split())

# map_file.close()

map_file = open('map-1.txt','r')

for line in map_file:
    current_map2.append(line.strip())

map_file.close()


map_max_x = 15
map_max_y = 15

# print('Map 1 : ', current_map)
print('Map 2 : ',current_map2)

for x in range(map_size):
    for y in range(map_size): 
        # print('ligne', i+1, current_map[i][0][j])
        print(f'case x={x},y={y}', current_map2[x][y])

