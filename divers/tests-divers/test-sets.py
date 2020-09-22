# source
# https://medium.com/better-programming/a-visual-guide-to-set-comparisons-in-python-6ab7edb9ec41


# les variables set
set_ref = {(1, 3)}
set_search = {(1, 3)}

# je verifie le type
print(type(set_ref))
print(type(set_search))

# fonction issubset() pour savoir si set_search est dans set_ref
result = set_search.issubset(set_ref) 

print(result)


# tests sur ma fonction pour p3

def is_special_cell(cell_pos):
        """ Determine if the cell is special """
        print(cell_pos)
        print(start)
        print(type(cell_pos))
        print(type(start))
        a = cell_pos.issubset(start)
        print(a)
        if cell_pos.issubset(start) == True:
            print('it is the start')
        # elif position in self.goal:
        #     print('it is the goal')
        # elif position in self.items:
        #     print('there are a item')
        else:
            print('nothing special')


start = {(0, 3)}
cell_pos = {(0, 3)}

is_special_cell(cell_pos)