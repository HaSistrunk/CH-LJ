#You had a list of URIs. So convert the list into a string so you can
#search for the names using regular expressions:

import re

#convert list into string for regex. Add space between each object to assist compile
chstring = ' '.join(name_of_your_list)

#print (name_of_your_list)

#compile pattern to find only names (The names appear to all start with capital letters,
#and I don't see any other capital letters in the CH data set of name URIs. So this pulls out
#a string from the first capital letter until a space, which you now have between each URI)

x = re.compile('([A-X][^\s]+)')

#search method
m = x.findall(chstring)

for person in m:
    print (person)


#you may have to refine the regular expression parameters, but that was my idea on how to isolate
#these names.
