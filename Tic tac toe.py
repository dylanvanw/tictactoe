import IPython.display as display
from IPython.display import clear_output

#constants
NUMBER_COLUMNS_ROWS = 3
PLAYER_2_CHAR = "x"
PLAYER_1_CHAR = "o"
MIN = 1

#text constants
START_TIC_TAC_TOE = "Welcome to tic tac toe"
ANOTHER_GAME = "Do you want to play again?"
ASK_YES_NO = "Type yes or no:"

TURN_PLAYER_2 = "Player 2, it is your turn"
ASK_INPUT ="on what coordinate do you want to place your character: "
TURN_PLAYER_1 = "Player 1, it is your turn"
ERROR_MESSAGE ="Something went wrong"
FIRST_GAME_MESSAGE = "Player 1 is \'o\', Player 2 is \'x\' "
BOARD_FULL_MESSAGE = "The board is full, it's a tie."
BYE_MESSAGE = "Thank you for playing."

"""
maak een overzicht op papier van welke functies ik heb en welke coresponderen met welke hij zei dat ik moest maken
Maak hier een overzich van op papier. Kijk welke je moet toevoegen voor een volwaardig programma en ga nog 
is door het programma heen om te kijken of volgorde van alles klopt enzo en of methodes niet veel mooier en 
efficienter gemaakt kunnen worden.
"""

#misschien later ook nog een feature toevoegen waardoor je je eigen character kan kiezen

def print_board(matrix):
    for i in range(NUMBER_COLUMNS_ROWS):
        for j in range(NUMBER_COLUMNS_ROWS):
            if j == NUMBER_COLUMNS_ROWS -1:
                print(matrix[i][j])
            else:
                print(matrix[i][j] + "|", end="")


def is_in_range():
    pass

def ask_coordinate():
    pass

def start_a_game():
    print(FIRST_GAME_MESSAGE)
    #create game object. every time a new game is made is the other deleted or will it flote in memory. If it is how to prevent this ask dad
    #determine who starts
    while(True):
        #print board
        #print ... it is your turn
        #ask clean input and if the place is free
        #game.make_move(input)
        #is_win = game.check_win() . ask dad on style of OOP, Is that if statement with a boolean from the object the right way or is there a better one
        #is_tie = game.check_tie()
        if is_win or is_tie:
            #say end of game
            #print last board
            #say who won or that its a tie





def start_tictactoe():
    print(START_TIC_TAC_TOE)
    while(True):
        start_a_game()
        print(ANOTHER_GAME)
        print(ASK_YES_NO)
        #get clena input yes or no. Make sure it does not do \n to write input
        if y_or_n == "y":
            continue
        else:
            break
    else:
        print(BYE_MESSAGE)

if __name__ == '__main__':
    start_tictactoe()