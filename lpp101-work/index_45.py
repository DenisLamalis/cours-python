# Zip / Unzip

# nums = [1,2,3,4] 
# letters = ['a','b','c','d']
# names =['John','Eric','Michael','Graham','Joe']
# combo = zip(nums,letters)
# print(combo)

# nums = '1234' 
# letters = ['a','b','c','d']
# names =['John','Eric','Michael','Graham','Joe']
# combo = list(zip(nums,letters,names))
# print(combo)

# num,let,nam =zip(*combo)                            #unpacking
# print(num, let, nam)

keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'

keys = keys.split()                                 #split on space
values = values.split()
print(keys,values)

en_sv_dict = dict(zip(keys,values))                         #do the same think
print(en_sv_dict)
new_dict = {key:value for key,value in zip(keys,values)}    #do the same think
print(new_dict)

en,sv = list(en_sv_dict.keys()),list(en_sv_dict.values())   #break again lists
print(en,sv)
en1,sv1 = zip(*en_sv_dict.items())                          #break other method
print(en1,sv1)