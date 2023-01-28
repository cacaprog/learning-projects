""" Rock, Paper, Scissor, the classic game!
Number #59 of Big Book of Python Projects
"""

import random, time, sys

print('''Welcome to Rock, Paper, Scissor.
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
''')

# Keep track of number os wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # Main game loop
    while True: # keep asking untill player enter R, P, S, or Q.
        print('{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))
        print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            break
        else:
            print('Type one of R, P, S, or Q.')

    # Display what the player chose

    if playerMove == 'R':
        print('Rock versus...')
        playerMove = 'ROCK'
    elif playerMove == 'S':
        print('Scissors versus...')
        playerMove = 'SCISSORS'
    elif playerMove == 'P':
        print('Paper versus...')
        playerMove = 'PAPER'

    # Count to three with dramatic pauses:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # Display the computer move
    random_number = random.randint(1, 3)
    if random_number == 1:
        computerMove = 'ROCK'
    elif random_number == 2:
        computerMove = 'PAPER'
    elif random_number == 3:
        computerMove = 'SCISSORS'
    print(computerMove)
    time.sleep(0.5)

    # Display and record win / losses / ties
    if playerMove == computerMove:
        print('It\'s a tie!')
        ties += 1
    elif playerMove == 'ROCK' and computerMove == 'SCISSORS':
        print('You win!')
        wins += 1
    elif playerMove == 'PAPER' and computerMove == 'ROCK':
        print('You win!')
        wins += 1
    elif playerMove == 'SCISSORS' and computerMove == 'PAPER':
        print('You win!')
        wins += 1
    elif playerMove == 'ROCK' and computerMove == 'PAPER':
        print('You lose!')
        losses += 1
    elif playerMove == 'PAPER' and computerMove == 'SCISSORS':
        print('You lose!')
        losses += 1
    elif playerMove == 'SCISSORS' and computerMove == 'ROCK':
        print('You lose!')
        losses += 1

