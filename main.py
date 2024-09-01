import random

def winner(player, computer):

    if((player == 'rock' and computer == 'scissors') or (player == 'scissors' and computer == 'paper') or (player == 'paper' and computer == 'rock')):
        return True
    else:
        return False
    
def play():
    computer = random.choice(['rock', 'paper', 'scissors'])
    player = input('rock, paper or scissors ?: ')

    if(player != 'rock' and player != 'paper' and player != 'scissors'):
        print('Wrong Input')
        play()

    if(player == computer):
        print('Draw')
    elif(winner(player, computer)):
        print("You Won")
    else:
        print("Computer Won")

    choice = input("Do you want to play again? yes or no ?: ")
    if(choice == 'yes'):
        play()

if __name__ == '__main__':
    play()
        

