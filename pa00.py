
# Programmers:  Paige Ronan
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 9/18/24
# Programming Assignment:  PA00
# Problem Statement:  Calculating the amount of grams and teaspoons are needed
#  when given the amount of cups
# Data In: How many cups are needed?
# Data Out:  The conversion of cups to grams and teaspoons
# Credits: Internet for conversion

#ask user how many cups are needed
cups = int(input('How many cups are needed?'))

#convert the amount of cups to the amount of grams and teaspoons
cup_to_gram = cups * 250
cup_to_teaspoon = cups * 16

#output the conversion
print(cups, 'cups converts to', cup_to_gram, 'grams and', cup_to_teaspoon, 'teaspoons')