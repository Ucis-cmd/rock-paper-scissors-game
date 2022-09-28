import random
turns = ['rock', 'paper', 'scissors']
human_turns = []
computer_turns = []
who_wins = []

while(True):
    human_turn = input("Enter your turn, or type exit: ")
    computer_turn = random.choice(turns)

    if human_turn == 'exit':
        print('Thank you for playing! Bye bye')
        break

    human_turns.append(human_turn)
    computer_turns.append(computer_turn)

    print(f'Human:{human_turn} vs. Computer:{computer_turn}')
    if human_turn == computer_turn:
        print('Draw!')
        who_wins.append("Draw")
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('Human wins!')
        who_wins.append("Human")
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('Human wins!')
        who_wins.append("Human")
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('Human wins!')
        who_wins.append("Human")
    else:
        print('Computer wins!')
        who_wins.append("Computer")

print(f"played games: {len(human_turns)}")
print(human_turns)
print(computer_turns)
print(who_wins)
