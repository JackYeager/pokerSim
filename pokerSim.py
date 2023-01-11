import random

deck = []
drawn = []
table = []
players = []

class Card:
    def __init__(self, val, suit) -> None:
        self.val = val
        self.suit = suit

def initDeck():
    deck.append(Card('A', 'H'))

    for i in range(9):
        deck.append(Card(i + 2, 'H'))
    
    deck.append(Card('J', 'H'))
    deck.append(Card('Q', 'H'))
    deck.append(Card('K', 'H'))

    deck.append(Card('A', 'D'))

    for i in range(9):
        deck.append(Card(i + 2, 'D'))

    deck.append(Card('J', 'D'))
    deck.append(Card('Q', 'D'))
    deck.append(Card('K', 'D'))

    deck.append(Card('A', 'S'))

    for i in range(9):
        deck.append(Card(i + 2, 'S'))

    deck.append(Card('J', 'S'))
    deck.append(Card('Q', 'S'))
    deck.append(Card('K', 'S'))

    deck.append(Card('A', 'C'))

    for i in range(9):
        deck.append(Card(i + 2, 'C'))

    deck.append(Card('J', 'C'))
    deck.append(Card('Q', 'C'))
    deck.append(Card('K', 'C'))

def drawCard(): 
    c = random.randint(0, 51)
    allPlayed = False

    while c in drawn:
        c = random.randint(0, 51)
        if len(drawn) == 52:
            allPlayed = True
            break
    
    if allPlayed:
        return
    else:
        drawn.append(c)
        return deck[c]

def printPlayers():
    for i, p in enumerate(players):
        print("P" + str(i + 1) + " ", end="")
        print(str(p[0].val) + str(p[0].suit), str(p[1].val) + str(p[1].suit))

def printTable():
    for c in table:
        print(str(c.val) + str(c.suit), " ", end="")
    print()

def drawTable():
    print("FLOP")
    table.append(drawCard())
    table.append(drawCard())
    table.append(drawCard())
    printTable()
    input()

    print("TURN")
    table.append(drawCard())
    printTable()

    input()
    print("RIVER")
    table.append(drawCard())
    printTable()

# ToDo: this function, determine best hand given the table and two cards
def determineHand():
    return
initDeck()
  
random.shuffle(deck)

players.append((drawCard(), drawCard()))
players.append((drawCard(), drawCard()))
players.append((drawCard(), drawCard()))
players.append((drawCard(), drawCard()))
players.append((drawCard(), drawCard()))

printPlayers()

print()
print()

drawTable()