import json
import re

p1deck = []
p2deck = []

with open('22/input.txt', 'r') as fp:
    data = fp.read().split('\n')
        
def draw_cards():
    global p1deck, p2deck, data

    p1deck = []
    p2deck = []

    for line in data:
        if line == '':
            continue
        if line == "Player 1:":
            mode = 'p1'
        
        elif line == "Player 2:":
            mode = 'p2'
        
        else:
            if mode == 'p1':
                p1deck.append(int(line))
            elif mode == 'p2':
                p2deck.append(int(line))

winner = None

def combat_round():
    global p1deck, p2deck, winner

    p1 = p1deck.pop(0)
    p2 = p2deck.pop(0)

    if p1 > p2:
        p1deck.extend(sorted([p1, p2], reverse=True))
    elif p2 > p1:
        p2deck.extend(sorted([p1, p2], reverse=True))

    if len(p1deck) == 0:
        winner = 'p2'
        
    if len(p2deck) == 0:
        winner = 'p1'

def calc_score(deck):
    score = 0
    i = 1
    while len(deck) > 0:
        score += i*deck.pop()
        i += 1

    return score

# Part1
draw_cards()

while winner is None:
    combat_round()

if winner == 'p1':
    score = calc_score(p1deck)
    print('Player 1 won with a score of: %d' % score)

elif winner == 'p2':
    score = calc_score(p2deck)
    print('Player 2 won with a score of: %d' % score)



# Part 2
def recursive_combat_game(p1deck, p2deck, gamelevel=1):
    deckhistory = set()
    winner = None
    emptydeck = False

    while emptydeck == False:
        decktuple = tuple([tuple(p1deck), tuple(p2deck)])
        if decktuple in deckhistory:
            return 'p1', p1deck, p2deck
        else:
            deckhistory.add(decktuple)

        p1 = p1deck.pop(0)
        p2 = p2deck.pop(0)

        if p1 <= len(p1deck) and p2 <= len(p2deck):
            winner = recursive_combat_game(p1deck.copy()[:p1], p2deck.copy()[:p2], gamelevel=gamelevel+1)[0]

        else:
            if p1 > p2:
                winner = 'p1'

            elif p2 > p1:
                winner = 'p2'

        if winner == 'p1':
            p1deck.extend([p1, p2])

        if winner == 'p2':
            p2deck.extend([p2, p1])

        if len(p1deck) == 0 or len(p2deck) == 0:
            emptydeck = True

    return winner, p1deck, p2deck



draw_cards()
winner, p1deck, p2deck = recursive_combat_game(p1deck.copy(), p2deck.copy())

print(p1deck)
print(p2deck)

if winner == 'p1':
    score = calc_score(p1deck)
    print('Player 1 won with a score of: %d' % score)

elif winner == 'p2':
    score = calc_score(p2deck)
    print('Player 2 won with a score of: %d' % score)