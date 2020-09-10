# Dictionaries

movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}

# print(movie)
# print(movie['title'])

# print(movie['budget'])
# print(movie.get('budget'))
# print(movie.get('budget','not found'))


# Update

# movie['title'] = 'The Holy Grail'
# print(movie.get('title'))

# movie['budget'] = 250000
# print(movie.get('budget'))

# movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})

# print(movie)


# Delete

# del movie['year']
# print(movie)

# year = movie.pop('year')
# print(movie)
# print(year)


# Informations

# print(movie)
# print(len(movie))
# print(movie.keys())
# print(movie.values())
# print(movie.items())


for key in movie:
    print(key)

for key, value in movie.items():
    print(key, value)

