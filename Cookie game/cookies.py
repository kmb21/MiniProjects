"""
This is a program that executes a cookie game model in which \
two users keep on removing cookies till there are none left in the jar
"""
def welcome():
   print("========================================")
   print("Welcome to the Cookie Jar game!")
   print("Whoever takes the last cookie has to go buy more, so the objective")
   print("of the game is to take as many cookies as you can without being\
 the")
   print("one who takes the last cookie. You also can't take more than\
 three")
   print("cookies at a time, since that's just rude.")
   print("========================================")
 
def is_valid(choice, min_val, max_val):
   """
   Checks a user choice to see if it's "valid" (i.e. between the bounds)
   parameters:
   choice (str) - the value to check
   min_val, max_val (int) - the lower and upper bounds of the "valid"
   range (inclusive)
   returns: (boolean) - True and choice if valid, False otherwise
   """
  
   if int(choice) in range(min_val, max_val + 1):

       return True and choice
   else:
        print("Sorry, you can't take %s cookies; value must be between \
between %s and %s" %(choice, min_val, max_val))
        return False
      
  
 
def get_choice(min_val, max_val, player, cookies):
    """
    This is a function that takes the number of cookies the players of the game\
    want to remove and if the number is greater than the number of cookies or\
    less than the minimum value of cookies players can select, it prompts the\
    player to make another choice.
    However if the number of cookies is less than 
    """
    choice = int(input("How many cookies does %s want to take? " %(player)))
    if cookies<max_val:
        max_val = cookies
    while is_valid(choice, min_val, max_val) == False or choice > cookies or\
        choice < (min_val):
        choice = int(input("Please enter a value between %d and %d: "\
        %(min_val, max_val)))

    else:
       return is_valid(choice, min_val, max_val)
 
def print_status(player, turn, cookies_left):
    """
    Prints the current status of the game
    """

    print("-------------------------------------------------------------")
    print("Turn %s - Jar contains %s cookies" %(turn, cookies_left))
    print("It's %s's Turn" %(player))
 
 
def get_player(turn, player):
    #keeps track of the player each time cookies are removed
    player = player[turn % 2]
    turn = turn + 1
    return player
 
def game_over(player1, player2):
    #Prints out the name of the player who loses and the player who wins
    print("### The cookie jar is empty! ###")
    print("%s takes the last cookie and must go buy another box!" %(player1))
    print("%s wins!" %(player2))
 
def play_game(players, min_take, max_take, cookies):
    #contains the main game loop and plays the game
    turn = 0
    while cookies > 0:
       player = get_player(turn, players)
       print_status(player, turn, cookies)
       number_taken = get_choice(min_take, max_take, player, cookies)
       cookies = cookies - number_taken
       turn = turn + 1
    player1 = get_player(turn, players)
    player2 = get_player(turn + 1, players)
    game_over(player2, player1)

    

 
def main():
   welcome()
   players = ["a", "b"]
   players[0] = input("What is the first player's name? ")
   players[1] = input("What is the second player's name? ")
 
   play_game(players, 1, 3, 12)
 
main()