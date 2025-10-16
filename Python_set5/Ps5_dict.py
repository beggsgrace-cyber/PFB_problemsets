#!/usr/bin/env python3
import sys
thing1 = sys.argv[1]

fav_things = {'book':'LOTR', 'song':'Happy','tree':'cedar'}
print(fav_things['book'])

fav_item = 'book'
print(fav_things[fav_item])
print(fav_things['tree'])

fav_things['organism'] = 'dog'
fav_item = 'organism'
print(fav_things[fav_item])

#use a for loop to print out each key and value of the dictionary
for thing in fav_things:
    print(thing, fav_things[thing])

#take a value from command line calling it thing1 instead of fav_thing
fav_things[thing1] = 'flowers'
print(fav_things [thing1])

#print the keys
print(fav_things.keys())

#change fav organism 9 and 10
fav_things['organism'] = 'cat'
fav_things[thing1] = 'friends'
print(fav_things[thing1])
print(fav_things)