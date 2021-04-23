### First step #######
print("Hello Universe")

# ---------- Tuples, Strings,  Loops ---------------
programming_languages = "Python ", "Java", "C++", "C#"  # Tuple
print(type(programming_languages))
for language in programming_languages:
    print(language)

# ------ List -------------------
l = [1,2,3,4,5]
print("The element to be print:")
print(l[1])
print(l[-1])
print(l[1:3])
print(l[2:])
print(l)
l[1]= 99
print(l)

# ----------- Tic-Tac-Toe ------------------
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]  # It's a list
print(game)
print(type(game))
print("   0  1  2")
count1 = 0

for row in game:
    print(count1, row)
    count1 = count1 + 1

# Python Built in function
def game_board():
    print("   0  1  2")
    for count2, row in enumerate(game):
        '''for item in row:
            print(item)'''
        print(count2, row)

x = game_board
game[0][1] = 1
x()

