"""
Maxwell Kumbong
5th November 2022
This a program that runs a game of dice between a human and computer 
where each player takes turns rolling a dice till one player wins
Goodluck!
"""
import random
def welcome():
    """
    It prints out a welcome message
    Parameters: 
        None
    Return:
        None
    Side effects: Prints a string of words
    """
    print("* BIG PIG *")
    print("")
    print("Welcome to Big Pig, the dice rolling game where players try to be the")
    print("first get 100 points! Players (you and the computer) will take turns")
    print("rolling two dice as many times as they want, adding all roll results to")
    print("a running total. Players lose their gained score for the turn if they")
    print("roll a 1.")

def player_turn(turn_number):
    """
    A function that returns whose turn it is to play. 
        Prints the dice_value and current round score
    """
    if turn_number % 2 == 0: #Ensures human starts since initial turn_numer = 0
        return "Player"
    else:
        return "Computer"

def getchoice(player_turn):
    """
    A function that validates and returns a string based on the user input
    If its the human's turn, it asks user for an input else, choice is roll(computer)
    Parameters:
        player_turn(string): It is either the player or the computer's turn
    Side effects: Asks for an  input(String)
    Return:
        An input(string) is player_turn is "player"
    """

    choice = input("What do you want to do: [r]oll or [h]old? ")
    while choice != "roll" and choice != "r" and choice != "h" and \
choice != "hold":#validates human input
        choice = input("What do you want to do: [r]oll or [h]old? ")
    return choice


def create_dice():
    """
    It creates two lists{1-6} if choice is roll and returns a list of two random\
    values, one from each of the lists
    Parameters: 
        None
    side effects:
        None
    Return:
        It returns a list with 2 random values from lists
    """
    dice1 = random.randrange(1, 7) #stores a random number in dice1
    dice2 = random.randrange(1, 7)
    return [dice1, dice2]

def human_score(player_turn, choice):
    """
    It sums dice value if both values are not equal, if dice values
    are both 1, sum = 25 if dice values are equal but not 1, sum is 
    double its valueif one dice value is 1 and the other is not, sum = 0
    Parameters:
        player_turn is a string(either Computer or Player)
        choice is a string(either to roll or hold)
    Side effects:
        Prints the dice_value and current round score
        And big pig if sum = 0 at the end
    Return:
        Sum of dice value based of conditions and the player_turn
    """
    sum = 0
    #The order of the conditions ensures that all conditions are respected
    while choice == "roll" or choice == "r":
        dice_value = create_dice()
            
        if dice_value[0] == 1 and dice_value[1] == 1:
            sum += 25
            print("%s rolled [%d, %d], current round score: %d"\
                %(player_turn, dice_value[0], dice_value[1], sum))
            
        elif dice_value[0] == dice_value[1]:
            sum += 2*(dice_value[0] + dice_value[1])
            print("%s rolled [%d, %d], current round score: %d"\
                %(player_turn, dice_value[0], dice_value[1], sum))
        
        elif (dice_value[0] > 1 and dice_value[1] > 1):
            sum += dice_value[0] + dice_value[1]
            print("%s rolled [%d, %d], current round score: %d"\
                %(player_turn, dice_value[0], dice_value[1], sum))     
            
        elif (dice_value[0] == 1 or dice_value[1] == 1):
            sum = 0
            print("%s rolled [%d, %d], current round score: %d"\
                %(player_turn, dice_value[0], dice_value[1], sum))
            print("Big Pig!")
            return sum
            
        choice = getchoice(player_turn)  
        
    print("%s holds" %(player_turn))
    return sum

    
def computer_score(player_turn, choice, human_gamescore, computer_gamescore):
    """
    It sums dice value if both values are not equal, if dice values
    are both 1, sum = 25 if dice values are equal but not 1, sum is 
    double its valueif one dice value is 1 and the other is not, sum = 0
    
    Parameters:
        player_turn is a string(either Computer or Player)
        choice is a string(either to roll or hold)
        human_gamescore is an integer(Current score of human in game)
        computer_gamescore is an integer(Current score of computer in game)
    Side effects:
        Prints the dice_value and current round score
        And big pig if sum = 0 at the end
    Return:
        Sum of dice value based of conditions and the player_turn"""
    sum = 0
    while choice == "roll" or choice == "r":
        dice_value = create_dice()
            
        if dice_value[0] == 1 and dice_value[1] == 1:
            sum += 25
            print("%s rolled [%d, %d], current round score: %d"\
                %(player_turn, dice_value[0], dice_value[1], sum))
            
        elif dice_value[0] == dice_value[1]:
            sum += 2*(dice_value[0] + dice_value[1])
            print("%s rolled [%d, %d], current round score: %d"\
                %(player_turn, dice_value[0], dice_value[1], sum))
        
        elif (dice_value[0] > 1 and dice_value[1] > 1):
            sum += dice_value[0] + dice_value[1]
            print("%s rolled [%d, %d], current round score: %d"\
                %(player_turn, dice_value[0], dice_value[1], sum))     
            
        elif (dice_value[0] == 1 or dice_value[1] == 1):
            sum = 0
            print("%s rolled [%d, %d], current round score: %d"\
                %(player_turn, dice_value[0], dice_value[1], sum))
            print("Big Pig!")
            return sum
        
        if human_gamescore < 100 and sum <20:
            choice = "roll"
        elif human_gamescore>100 and\
human_gamescore > (sum + computer_gamescore) :
            choice = "roll"
        else:
            choice = "hold"
    print("%s holds" %(player_turn))
    return sum    
  
 
def game_end(computer_gamescore, human_gamescore):
    """
    It prints the player who won and the final scores of the computer and human
    Parameters:
        human_gamescore is an integer(Current score of human in game)
        computer_gamescore is an integer(Current score of computer in game)        
    Side effects:
        Prints an exit message displaying the winner
    Return:
        None
    
    """
    if human_gamescore > computer_gamescore:
        print("human wins [%d, %d]!"\
            %(human_gamescore, computer_gamescore))
    else:
        print("Computer wins [%d, %d]!"\
            %(human_gamescore, computer_gamescore))
def main():
    welcome()
    #displays welcome message
#initialize human and computer game scores
    computer_gamescore = 0
    human_gamescore = 0
    turn = 0 #Ensures that human plays first. See player_turn() function
    while human_gamescore < 100 and computer_gamescore<100:
        print("")
        print("--------------------------------------------------")
        print("Player has %d and computer has %d" %(human_gamescore,\
computer_gamescore))
        player = player_turn(turn)
    #if turn % 2 == 0, human's turn
    #else computer's turn
    #prints whose turn it is

        dice_value = create_dice()
        if player == "Player":
            choice = getchoice(player)
#asks the user for an input, either roll or hold
#returns input            
            human_roundscore = human_score(player, choice)
        else:
            choice = "roll" #ensures computer rolls when human score<100
            computer_roundscore = computer_score(player, choice, human_gamescore,\
computer_gamescore)
    #creates two lists{1-6} if choice is roll
    #returns a random value from each list

        
    #sums dice value if both values are not equal
    #if dice values are both 1, sum = 25
    #if dice values are equal but not 1, sum is double its value
    #if one dice value is 1 and the other is not, sum = 0
    #Adds sum to the player game_score
         
        
    #sums dice value if both values are not equal
    #if dice values are both 1, sum = 25
    #if dice values are equal but not 1, sum is double its value
    #if one dice value is 1 and the other is not, sum = 0
    #Adds sum to the player game_score

        if player == "Player":
            human_gamescore += human_roundscore
        else:
            computer_gamescore += computer_roundscore
        turn += 1
    if player == "Player": #ensures that computer is the last to play, before \
        #winner is decided
        player = "Computer"#ensures computer plays last
        choice = "roll"#ensure computer tries to beat human's score
        print("")
        print("--------------------------------------------------")
        print("Player has %d and computer has %d" %(human_gamescore,\
computer_gamescore))
        computer_roundscore = computer_score(player, choice, human_gamescore, \
computer_gamescore)
        computer_gamescore += computer_roundscore            
    
    game_end(computer_gamescore, human_gamescore)#determines winner of game

main()