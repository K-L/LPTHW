### ex13.py

from sys import argv

script, first, second, third = argv

print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third

### Part B - combine raw_input with argv to make a script that gets more input from a user
first = raw_input("Your first variable is: ")
second = raw_input("Your second variable is: ")
third = raw_input("Your third variable is: ")

print "You have supplied the following values: " + first, second, third
