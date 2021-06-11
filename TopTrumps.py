#####################################################################################################
# Pokemon Project
# Authors: Daisy Matthews, Ellie Watts, Dzhemma Ruseva
# Since: 27th of March
#####################################################################################################

# imported libraries for generating random number and get a request from the Pokemon API
import requests
import random


# A function to generate a random pokemon's information
def pokemon():

    # Random generating of the pokemon's ID
    random_number = random.randint(1, 151)

    # Creating the URL link for the request
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(random_number)

    # Taking the information from the API
    response = requests.get(url)

    # Converting the response in a JSON file (Dictionary)
    pokemon_info = response.json()

    # Creating a dictionary with the wanted data
    data = {
        "id": pokemon_info["id"],
        "name": pokemon_info["name"],
        "height": pokemon_info["height"],
        "weight": pokemon_info["weight"],
        "base experience": pokemon_info["base_experience"]
    }

    # return this dictionary when the function is called
    return data


# Asking the individual how many rounds they want
rounds = int(input("How many rounds do you want to play? "))

# Setting the score at 0
opponent_win = 0
player_win = 0

# A loop to simulate the rounds
for round in range(1, rounds + 1):
    # Assigning the information from the function to the players
    player_data = pokemon()
    opponent_data = pokemon()

    # Printing the data of the user
    print("Player's data: " + str(player_data))
    print("\n")
    # Ask the user which value to compare in the fight
    option = input("What stat do you want to use?(height,weight,base experience) ")

    # Comparing the two choice and update the scores
    if player_data[option] == opponent_data[option]:
        player_win = player_win + 0.5
        opponent_win = opponent_win + 0.5

    elif player_data[option] > opponent_data[option]:
        player_win = player_win + 1

    else:
        opponent_win = opponent_win + 1
    print("Opponent's data: " + str(opponent_data))

    # It looks cool
    print("\n--------------------------------------------------------------------------------------\n")

# Printing the outcome of the game
if player_win == opponent_win:
    print("It is a draw with a score of {}".format(player_win))
elif player_win < opponent_win:
    print("The opponent has won with a score of {}".format(opponent_win))
else:
    print("You have won with a score of {}".format(player_win))
