def cities(country, *cities):
    print(country, cities)
    print("Type is ", type(cities))

cities("France")
# France ()
# Type is  <class 'tuple'>

cities("France", "Paris", "Mollégès", "Bourg la Reine")
# France ('Paris', 'Mollégès', 'Bourg la Reine')
# Type is  <class 'tuple'>


def list_songs(**songs):
    print(songs)
    print("Type is ", type(songs))

list_songs()
# {}
# Type is  <class 'dict'>

list_songs(adele_songs = ["Hello", "Someone like you"], backstreet_boys_songs = ["Larger than life", "I want it that way"])
# {'adele_songs': ['Hello', 'Someone like you'], 'backstreet_boys_songs': ['Larger than life', 'I want it that way']}
# Type is  <class 'dict'>