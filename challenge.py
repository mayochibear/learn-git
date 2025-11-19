capitals = {
    "USA": 'Washington D.C',
    "India": 'New Delhi',
    "China": 'Beijing',
    "Russia": 'Moscow'
}

capitals.get("USA") #Use this to get the value if the key might exist, RETURNS NONE OR DEFAULT. when you're not sure or want a default value instead of an error.
capitals.update({"Germany": "Berlin"}) #add another pair to dictionary
capitals.update({"USA": "Berlin"}) #if the key already exists, it will change the value of the existing key
capitals.pop("China") #removes pair using key
capitals.popitem() #doesnt need a key, it will remove the last pair in dict
capitals.keys() #returns all the keys in the dict
capitals.values() #return all the values in the dict
capitals.items() #return a dict obj that looks a 2d list of tuples
capitals["USA"] #use this to get the value using the key if you're sure that key exists. ERROR IF IT DOESNT EXISTS

#for key in capitals:
    # print(capitals[key])