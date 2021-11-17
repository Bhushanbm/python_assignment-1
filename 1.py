lion = 2
white_tiger = 2
red_deer = 50
elephant = 10
spider_monkey = 100
zebra = 17
rhinoceroses = 10
black_panther = 10
harpy_eagles = 12
white_backed_vulture = 5
herbivorous = lion, white_tiger, rhinoceroses, black_panther, harpy_eagles;
carnivorous = red_deer, elephant, spider_monkey, zebra;

print("There are", lion, "lions.")
print("There are",white_tiger,"White tigers .")
print("There are",red_deer,"Red deers.")
print("There are",elephant,"Elephants .")
print("There are",spider_monkey,"Spider monkeys .")
print("There are",zebra,"zebras.")
print("There are",rhinoceroses,"Rhinoceroses.")
print("There are",black_panther,"Black panthers.")
print("There are",harpy_eagles,"Harpy eagles.")
print("There are",white_backed_vulture,"White backed vultures .")
h = sum(herbivorous);
print("There are total",h, "Herbivorous animals")
c= sum(carnivorous)
print("There are",c,"Carnivorous animals")
