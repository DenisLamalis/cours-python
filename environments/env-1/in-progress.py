
# create the map

current_map = []
current_map2 = []

map_file = open('map-1.txt','r')

for line in map_file:
    current_map.append(line.strip().split())

map_file.close()

map_file = open('map-1.txt','r')

for line in map_file:
    current_map2.append(line.strip())

map_file.close()


map_size = 15

print('Map 1 : ', current_map)
print('Map 2 : ',current_map2)

for i in range(map_size):
    for j in range(map_size): 
        # print('ligne', i+1, current_map[i][0][j])

