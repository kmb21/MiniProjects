# 1. initialize variables
# 2. read the puzzle
# 3. play until win, lose or quit
    # a. display partially filled puzzle
    # b. choose spin, guess, or quit
        # Spin: spin the wheel; work out more details
        # Guess: ask user for solution. win if correct, 
        #        else lose a token
        # Quit: game over
    # c. out of tokens? game over
# 4. print prize information

def main():
    # 1. initialize variables
    points = 0
    tokens = 5
    guessed_letters = []

    # 2. read the puzzle
    puzzle = read_puzzle()

    # 3. play until win, lose or quit
    game_over = False
    while not game_over:
        # a. display partially filled puzzle
        display_filled_puzzle(puzzle, guessed_letters)

        # b. choose spin, guess, or quit
        turn = choose_turn()

        if turn == 'spin':
            # Spin: spin the wheel; work out more details
            value = spin_wheel()
            # more details to come
        elif turn == 'guess':
            # Guess: ask user for solution. win if correct, else lose a token
            correct = attempt_to_solve(puzzle)
            if correct == True:
                game_over = True
            else:
                tokens = tokens - 1
        else: 
            # Quit: game over
            game_over = True

        # c. out of tokens? game over
        if tokens == 0:
            game_over = True

    # 4. print prize information
    print("Prize information")
    
def read_puzzle():
    """
    Reads a puzzle from a file and prints the category
    Parameters: None
    Returns: The puzzle as a string
    Side effects: Prints the category
    """
    print("-> read_puzzle")
    print("The category is: Activity")
    return "STUBBING FUNCTIONS"

def display_filled_puzzle(puzzle, guessed_letters):
    """
    Prints the partially filled puzzle
    Parameters:
      puzzle: a string representing the puzzle
      guessed_letters: list of letters the user has already guessed
    Returns: None
    Side effects: Prints the filled puzzle
    """
    print("-> display_filled_puzzle")
    print("----- -----") # a possible filled puzzle

def choose_turn():
    """
    The player will choose to Spin, Guess, or Quit. This function
    will not return until a valid input is provided.
    Parameters: None
    Returns: one of "spin", "guess", or "quit" (all lowercase)
    Side effects: Interactive input
    """
    print("-> choose_turn")
    turn = input("Do you want to Spin, Guess or Quit: ")
    return turn.lower()

def spin_wheel():
    """
    Spins the wheel and returns the point value that we
    land on. Point values are integers 0 or larger. 
    A point value of 0 will be interpreted as BANKRUPT.
    Parameters: None
    Returns: point value, an integer
    Side effects: None
    """
    print("-> spin_wheel")
    return 250

def attempt_to_solve(puzzle):
    """
    The user attempts to guess the puzzle.
    Parameters: puzzle, a string representing the puzzle
    Returns: True if the guess is correct; False otherwise
    Side effects: interactive input
    """
    print("-> attempt_to_solve")
    guess = input("What is your guess? ")
    return False

main()