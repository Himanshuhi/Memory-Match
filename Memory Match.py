import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)

cards = []
for number in numbers:
    cards.append({'number': number, 'matched': False})

def print_board(cards):
    for i in range(0, len(cards)):
        if cards[i]['matched'] == True:
            print(str(cards[i]['number']).rjust(2), end=' ')
        else:
            print('##', end=' ')
        if (i + 1) % 4 == 0:
            print()

def check_match(cards, index1, index2):
    if cards[index1]['number'] == cards[index2]['number']:
        cards[index1]['matched'] = True
        cards[index2]['matched'] = True
        return True
    else:
        return False

num_matches = 0
player1_score = 0
player2_score = 0

while num_matches < 8:
    print_board(cards)
    print()

    print("Player 1's turn")
    index1 = int(input('Enter the index of the first card to flip(0-15): '))
    index2 = int(input('Enter the index of the second card to flip(0-15): '))
    if check_match(cards, index1, index2):
        print('Match!')
        player1_score += 1
        num_matches += 1
    else:
        print('No match.')
    
    print_board(cards)
    print()

    print("himanshu turn")
    index1 = int(input('Enter the index of the first card to flip(0-15): '))
    index2 = int(input('Enter the index of the second card to flip(0-15): '))
    if check_match(cards, index1, index2):
        print('Match!')
        player2_score += 1
        num_matches += 1
    else:
        print('No match.')

print('Game over!')
print('Player 1 score:', player1_score)
print('Player 2 score:', player2_score)
if player1_score > player2_score:
    print('Player 1 wins!')
elif player2_score > player1_score:
    print('Player 2 wins!')
else:
    print('Tie game!')

    
 #to exit press ctrl+c   
