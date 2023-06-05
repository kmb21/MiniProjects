from random import*
class Ludo():
   players_houses = {}
   def __init__(self, player_name, house, pawns):
       """
       Stores player name and houses in a dictionary for future reference or printing
       """
       self.player = player_name
       self.house = house
       self.pawns = pawns
       self.retired_pawns = 0
       
       self.pawn1 = 0
       self.pawn2 = 0
       self.pawn3 = 0
       self.pawn4 = 0
       self.pawn5 = 0
       self.total = self.pawn1 + self.pawn2 + self.pawn3 + self.pawn4 + self.pawn5

   def roll_dice(self):
       """
       Simulates two dice and generates random values for them
       Prints which player rolled dice and sums the value of dice
       Returns sum at the end
       """
       sum = 0
       dice1 = randrange(1, 7)
       dice2 = randrange(1, 7)
       print("%s rolled [%d, %d]"%(self.player, dice1, dice2))
          
       sum += dice1 + dice2
       return sum
  
   def conditions(self, sum):
#Do for computer later
 
       """
       player chooses which pawns to move
      
       Args:
           sum(int): return value from roll_dice
       """
       print()
       
       lst = [self.pawn1, self.pawn2, self.pawn3, self.pawn4, self.pawn5]
       privatesums = []
 
       for item in lst:
           if item >= 52:
               index = lst.index(item)
               print("%s%d has completed journey. "%(self.house, index+1))
               self.retired_pawns += 1
               lst.remove(item)
      
       n = self.pawns
       if n == 5:
           return lst
       if self.player == "Computer":
           sum_strip = 0
           
           if sum % 2 == 0:
               sum_strip = sum // (6-n)
           else:
               sum_strip = sum // (6-n)
               sum_strip += 1
               
               
           for number in range(1, 6-n):
               lst[number] += sum_strip
               print("%s moves %s%d by %d"%(self.player, self.house, number, sum_strip))
           
       else:          
           print("Available pawns: ")
           for number in range(1, 6 - n):
               print("%s%d"%(self.house, number))
           print("How do you want to move pawns: ")
           for item in range(1, 6-n):
            #gets the way player plans to move seeds
               movement1 = input("%s%d: "%(self.house, item))
               while movement1.isdigit() is False or int(movement1)>sum:
                   print("Please enter a valid number: ")
                   movement1 = input("%s%d: "%(self.house, item))
               print("%s moves %s%d %d times"%(self.player, self.house, number, int(movement1)))
               sum -= int(movement1)
               privatesums.append(int(movement1))
 
       for number in range(len(privatesums)):
           if (privatesums[number] + lst[number]) > 52:
               remains = 52 - lst[number]
               print("Sorry, you need to roll %d to complete pawns journey!"%remains)
           else:
               lst[number] += privatesums[number]
       return lst
       """ How this function works
       if len(privatesums) == 2:
           self.pawn1 += privatesums[0]
           self.pawn2 += privatesums[1]
     
       elif len(privatesums) == 3:
           self.pawn1 += privatesums[0]
           self.pawn2 += privatesums[1]
           self.pawn3 += privatesums[2]       
          
       elif len(privatesums) == 4:
           self.pawn1 += privatesums[0]
           self.pawn2 += privatesums[1]
           self.pawn3 += privatesums[2]  
           self.pawn4 += privatesums[3]  
          
       elif len(privatesums) == 5:
           self.pawn1 += privatesums[0]
           self.pawn2 += privatesums[1]
           self.pawn3 += privatesums[2]  
           self.pawn4 += privatesums[3]            
           self.pawn5 += privatesums[4]
      
       else:
           self.pawn1 += privatesums[0]  """
          
          
       
   """def game_status(self):
       
       #Gives a summary each player's stats during the game
       #Returns:
          #None
       
       remainder1 = 52 - self.pawn1
       remainder2 = 52 - self.pawn2
       remainder3 = 52 - self.pawn3
       remainder4 = 52 - self.pawn4
       remainder5 = 52 - self.pawn5
 
      
       print()
       print("-----------------------------------------------------------")
       print("%s has %d pawns left in captivity"%(self.player, self.pawns))
       lst = [remainder1, remainder2, remainder3, remainder4, remainder5]
       
       n = 0
       
       for item in lst:
           
           if item == 0:
               print("Pawn %s%d is still to be liberated"%(self.house, n))
 
           else:
               print("Movements left:  %s%d = %d movements"%(self.house, n+1, item))   
           
           n += 1"""
       #print("Movements left:  %s2 = %d movements"%(self.house, remainder2))
       #print("Movements left:  %s3 = %d movements"%(self.house, remainder3))
       #print("Movements left:  %s4 = %d movements"%(self.house, remainder4))
       #print("Movements left:  %s5 = %d movements"%(self.house, remainder5))
##create a method to add to steps(Done)
##A method which reduces pawns(Done)
##Store player data in a list to know which player's turn it is(Done)
      
   def get_name(self):
       return self.player
  
   def get_pawns(self):
       return self.pawns
  
   def get_total(self):
       return self.total
  
   def get_retired_pawns(self):
       return self.retired_pawns
 
   def update_dice(self, element):
 
       dice_value = element.roll_dice()
       while dice_value == 12:
           self.pawns -= 1
           dice_value = element.roll_dice()
       if self.pawns == 5:
           print("Oops, you didn't make it. Better Luck next time!")        
       else:
           return dice_value
           
   def secret_spot(self, lst):
       print()
       print("Capture spots: ")
       r = 40
       y = 4
       g = 18
       b = 29
       print("Y%d "%y)
       print("G%d "%g)
       print("B%d "%b)
       print("R%d "%r)
       print()
       for item in lst:
           if item == r and self.house != "R":
               print("Oops, trespassing in %s's house a pawn has been caputured"%self.house)
               self.pawns += 1
               print()
               print("Pawns to free: %d"%self.pawns)
 
           elif item == y and self.house != "Y":
               print("Oops, trespassing in %s's house, a pawn has been caputured"%self.house)
               self.pawns += 1
               print()
               print("Pawns to free: %d"%self.pawns)               
 
           elif item == g and self.house != "G":
               print("Oops, trespassing in %s's house, a pawn has been caputured"%self.house)
               self.pawns += 1
               print()
               print("Pawns to free: %d"%self.pawns)
 
           elif item == b and self.house != "B":
               print("Oops, trespassing in %s's house, a pawn has been caputured"%self.house)
               self.pawns += 1
               print()
               print("Pawns to free: %d"%self.pawns)   


           
       ##To win, player must roll the exact number left
def welcome():
   """
   prints welcome message
   """
   print()
   print("---------------------------------------------------------------------")
   print("Welcome to the game of Ludo!!!")
   print("Each Player has a house with 5 pawns")
   print("The first player to reach the move all five pawns to center wins")
   print("If a player rolls [6,6], they roll again and one pawn is in play")
   print("You can capture a pawn by moving into its position")
   print("Two pawns from the same house create a block")
   print("Whoof, so many rules......")
   print()
   print("Enjoy!!!!!")
   print("---------------------------------------------------------------------")
  
  
def players():
   #Must be 2-4 players
   """
   Asks if playing against computer or other opponents. If against opponents, asks
   for  names and stores names in a list
   Return:
       list of player names
   """
   players = []
  
   print()
  
   print("Choose designated letters for response")
   choice = input("Play against opponents(O) or computer(C): ")
   while choice.lower() not in ["c", "o"]:
       print()
       print("Please choose either O or C")
       print()
       #validates choice
       choice = input("Play against opponents(O) or computer(C): ")
  
   print()
   if choice.lower() == "c":
       player_name = input("Enter your name: ")
      
       players.append(player_name.title())
       players.append("Computer") 
      
      
       return players
   else:
       num_players = input("Number of players: ")
       while num_players.isdigit() is False:
           print()
           print("Please Enter a number in range 2 - 4")
           num_players = input("Number of players: ")
          
       while int(num_players) not in range(2, 5):
           print()
           print("Please Enter a number in range 2 - 4")
           num_players = input("Number of players: ")  
          
       for i in range(1, int(num_players)+1):
          
           print()
           player = input("Enter name %d: "%(i))
           players.append(player.title())
          
          
       return players
      
def house(players):
   #Use class to store players houses with their names
   """
   Asks player(s) to choose their caste(house)
   Uses class to store this data
   Returns a list of player data objects
   Args:
       players (list): A list with names of players
      
   """
   player_object = []
  
   print()
   print("Choose designated letters for response")
   print()
  
   print("Available houses: Yellow(Y), Green(G), Blue(B), Red(R)") 
   houses = ["Y", "G", "B", "R"]
   n = 0   
   for item in players:
       if item != "Computer":
           print()
           player_house = input("Choose a house %s: "%players[n])
          
          
           while player_house.capitalize() not in houses:
               print()
               print("Please enter a valid house")
               player_house = input("Choose a house %s: "%players[n])
          
           n += 1
          
           player_data = Ludo(item, player_house, 5)
          
           player_object.append(player_data)
           houses.remove(player_house.title())
      
       else:
           player_house = choice(houses)
           #randomly assigns computer a house from the modified list of houses
           
           player_data = Ludo(item, player_house, 5)
           player_object.append(player_data)
           houses.remove(player_house.title())
           
           
   return player_object


def winner(lst, objects):
    """
    Displays a final message concluding the game and declaring the winner
    Returns a string with the winnner
    """
    names = []
    print()
    max = 0
    for fig in range(len(lst)):
        if lst[fig] > lst[max]:
            max = fig

    winner_up = objects[max]
    print("Yayy!! %s wins!"%winner_up.get_name())
    user_objects.remove(objects[max])
    for item in objects:
        name = item.get_name()
        names.append(name)
    print()
    print("Better luck next time %s"%names)

if __name__ == "__main__":
   #Start with welcome, explain all rules
   #Get players, either computer or other oponents
   #Validate player info
   #Conditions for pawns(>0) for each player.Game runs on this
   #Use modulo to determine whose turn it is.
   ####First player to play is the player who rolls [6, 6] first
   #pawns can only be on board when a player rolls 6,6
   #After this, the player rolls again
   #Each time a player rolls 6,6, they can bring a new pawns on to the board
   #Then they roll again to choose number of steps
   #There should be special points(4 of them) on the board
   #If a player lands in special place, add pawns by 1
   #If a player rolls a 1-5 and does not have a pawn on the board, \
   #### then they cannot move and it is the next player’s turn.
   #If a player lands on the same space with another player's pawns, \
   ##### the other players pawns increases by 1
   #If a player has two pawns on the same space, it serves as a block
   #You can only pass a block if you land on the exact space
  
   welcome()
   #verify if player wants to play game
   print()
   play_exit = input("Play game or exit (Choose P or E): ")
   print()
   while play_exit.title() not in ["P", "E"]:
       play_exit = input("Play game or exit (Choose P or E): ")
   totalies = []  
   if play_exit.title() == "P":
       #get players
      users = players()
      #get players houses
      user_objects = house(users)
     
      sumss = 0
      max = user_objects[0].get_total()
      while max < 260:
          #get each player's status after running the game for all players each time
              
          for item in user_objects:
               print("%s's turn "%item.get_name())
               dice = item.update_dice(item)
               lst = item.conditions(dice)
               
               #item.secret_spot(lst)
               #item.game_status() 
                
          for number in range(len(user_objects)):
                if user_objects[number].get_total() > max:
                   max = user_objects[number].get_total()
                  
      for item in user_objects:
          tot_value = item.get_total()
          totalies.append(tot_value)
    
      winner(totalies, user_objects)
      print("It was a tough run! ")
      play_exit = input("Play game or exit (Choose P or E): ")
      print()
      while play_exit.title() not in ["P", "E"]:
          play_exit = input("Play game or exit (Choose P or E): ")
     
   else:
       print("Sorry to see you go.")
       print("Goodbye")
#####create a way to move seeds(Done)

#make list and put self.pawns in it\
#track sum in another function and remove self.pawns from list based on sum
