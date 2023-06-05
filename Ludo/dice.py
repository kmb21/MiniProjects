from random import *

"""
This is the backend code for the game of Ludo
"""   
def roll_dice(player_name):
    
    n = 1
    dice_total = 0
    dice1 = randrange(1, 7)
    dice2 = randrange(1, 7)

    dice_total += dice1 + dice2
    print("%s rolled"%player_name + " [%d, %d]"%(dice1, dice2))
    while dice1 == 6 and dice2 == 6:
        n += 1
        dice1 = randrange(1, 7)
        dice2 = randrange(1, 7)    
        dice_total += dice1 + dice2
        print("%s rolled "%player_name + "[%d, %d]"%(dice1, dice2), n, "times")    
    
    return dice_total
        
def welcome():
    """
    Prints the welcome message
    Return:
        a string
    """
    print("Welcome to the game of Ludo")
    option = input("Play against computer(C) or opponent(O)\n ***Choose corresponsing letter***:")
    while option not in ['C', 'O']:
        option = input("Play against computer(C) or opponent(O)\n ***Choose corresponsing letter***:")
    return option


def no_players():
    """
    Asks for the total number of players and validates the value
    Returns the number of players
    """
    no_players = input("Enter the number of players: ") 
    while no_players.isdigit() is False:
        no_players = input("Enter a valid number from 1 - 4: ")
    
    return int(no_players)

def player_names(no_players):
    """
    Generatesan input for names of players based on the number

    Args:
        no_players (str): The number of players
    """
    names = []
    for number in range(1, no_players + 1):
        name = input("Enter player %d's name: "%(number))
        names.append(name)
        
    return names 

        
def house(player_names):
    """
    Players choose their caste(Red, Blue, green or Yellow)
    Args:
        player_names(list):  A list of all player names
    """
    players_houses = {}
    print("Available houses: red, yellow, green, blue")
    for player_name in player_names:
        choice = input("Which house does %s choose: "%(player_name))
        choice.lower()
        while choice not in ["red", "yellow", "blue", "green"]:
            print("Available houses: red, yellow, green, blue")
            choice = input("Please enter an appropriate house: ")
            choice.lower()
        players_houses["%s" %player_name] = choice
        
    return players_houses

        
        

def dice():
    """
    Simulates two dice which can be rolled to generate random values
    Returns a list with both dice values
    """
    

    
if __name__ == "__main__":
    
    option = welcome()#prints welcome message explaining game
    if welcome == "C":
        player_steps = 0
        computer_steps = 0
        names = player_names(1)
        names.append("Computer")
        
        
    number_players = no_players()
    #create individual sums to total dice values inorder to count steps
    
    if number_players != "0":
        
        player_names(number_players)
          