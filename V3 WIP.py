import random

player_styles = {"wrestling": 1, "boxing": 2, "karate": 3}
player_moves = {"block": 7, "dodge": 8, "miss": 9}

player_health = 10
enemy_health = 10

# Functions
def player_turns():
    global enemy_health
    if style == 2:
        print("You have thrown a punch! ")
    elif style == 1:
        print("You have shot for a takedown! ")
    elif style == 3:
        print("You have thrown a kick! ")

    roll = random.randint(1, 10)

    if roll >= 7 and roll < 10:

        if roll == 7:
            print(f"{opponent} blocked your hit! ")
        elif roll == 8:
            print(f"{opponent} dodged your hit! ")
        elif roll == 9:
            print("You missed! ")
        
    else:
        print(f"Your hit has landed on {opponent}! ")
        enemy_health = enemy_health - 2
        print(f"{opponent}'s health is now {enemy_health}! ")

def enemy_turns():
    global player_health
    move = random.randint(1, 3)
    if move == 1:
        move2 = random.randint(5, 6)
        if move2 == 5:
            print(f"{opponent} has taken you down!")
            player_health = player_health - 2
            print(f"Your health is now {player_health}! ")
        elif move2 == 6:
            print(f"{opponent} has shot for a takedown but missed!")

    elif move == 2:
        move3 = random.randint(6, 7)
        if move3 == 6:
            print(f"{opponent} has punched you! ")
            player_health = player_health - 1
            print(f"Your health is now {player_health}! ")
        elif move3 == 7:
            print(f"{opponent} has thrown a punch but missed! ")

    elif move == 3:
        move4 = random.randint(7, 8)
        if move4 == 7:
            print(f"{opponent} has kicked you!")
            player_health = player_health - 2
            print(f"Your health is now {player_health}! ")
        elif move4 == 8:
            print(f"{opponent} has thrown a kick but missed!")

name = input("What is your name? ")
opponent = input("What is the name of your opponent? ")
print(f"{name} will now be fighting {opponent}!")

print(player_styles)

try:
    style = int(input("Pick a number to choose your style! "))

except ValueError:
    print("Error")

else:
    if style == 1:
        print("You have chosen wrestling! ")
    elif style == 2:
        print("You have chosen boxing! ")
    elif style == 3:
        print("You have chosen karate! ")
    else:
        print("Error")

    while player_health > 0 and enemy_health > 0:
        print("The fight starts! ")

        for turn1 in range(1, 3):
            player_turns()

        print(f"{opponent} gets ready for an attack! ")
        for turn2 in range(1, 2):
            enemy_turns()

        print("It is now your turn to attack! ")

        print(f"It is now {opponent}'s turn to attack! ") 

        if player_health <= 0:
            print("You died, game over.")
            break
        elif enemy_health <= 0:
            print("You won, game over.")
            break
