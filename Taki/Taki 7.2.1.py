import random

class Cardsdeck (object):
    def deck_of_cards (self):
        number = [(1), (2), (3), ('+3'), (4), (5), (6), (7), (9), ('Stop'), ('Plus'), ('Switch'), ('Taki')]
        # number is a list of the names of the cards
        superCards = [('Super Taki'), ('Change Color'), ('Change Color')]
        # supercards is a list of the super cards in the game
        red =['RED'] * 13
        green = ['GREEN'] * 13
        yellow = ['YELLOW'] * 13
        blue = ['BLUE'] * 13
        rgyb = ['RGYB'] * 3
        # every card has a color, so i made a list for every color
        cards = dict (enumerate (zip(number,red) + zip(number, green) + zip (number, yellow) + zip(number, blue) + zip(superCards, rgyb)+ zip(number,red) + zip(number, green) + zip (number, yellow) + zip(number, blue) + zip(superCards, rgyb)))
        # here i am creating a dictionary of all the cards
        # i use enumerate to add a number to each card so it will look like this: cards = {1:{'1','RED'},..)
        # so now i have a data base of the cards, i can call for a card with his key in the cards dictionary
        # print cards
        # print len(cards)
        self._cards = cards
        return self._cards
# Class "Cardsdeck" is the class where the game in making the cards deck.

class Players (object):

    def how_many_players (self):
        name_players = {}
        indic = True
        while (indic):
            try:
                num_of_players = input("How many players? ")
            except NameError:
                print "Numbers, not letters"
                continue
                # if the input is a letter it will raise a name error and ask again for number of players
                #it will ask for a number as long as the input is not a number
            except SyntaxError:
                continue
            else:
                break
        while num_of_players >10:
            try:
                if (num_of_players > 10):
                    raise IndexError
            except IndexError:
                print "To many players"
                num_of_players = input("How many players? ")
                # if the user's number is to high it will raise an error and ask for number of players
                # it will ask for a number as long as the input is not a number
                continue
            else:
                break
        while num_of_players < 2:
            try:
                if num_of_players < 2:
                    raise IndexError
            except IndexError:
                print "To few players"
                num_of_players = input("How many players? ")
                # if the user's number is to low it will raise an error and ask for number of players
                # it will ask for a number as long as the input is not a number
                continue
            else:
                break
        for i in range(num_of_players):
            name_players[i] = raw_input("Enter name: ")
        # from 1 to the number of players, it will ask for the name of the players and save it in a list
        players = [name_players, num_of_players]
        return players
# Class "Players" is the class where the game is asking for the number of players and their names

class Shuffled(object):

    def draw_to_players (self, players):
        num_of_cards = 1
        players_name = players[0]
        num_of_players = players[1]
        hands = {}
        deck = map (lambda x: x, xrange(110))
        deck = random.sample(deck, len(deck))
        # deck is a list of the numbers of the cards
        # deck = [1,2,3,4.....110]
        # i will each number in list deck as equal the key of a card in dict cards. that way i can use numbers to symbolizes cards
        # deck (1) = 1 = cards [1] = ('1', 'RED')
        # self._deck = deck
        for i in range(num_of_players):
            # from 1 to the number of players
            hand = []
            for x in range(8):
                # random_card = random.SystemRandom()
                # # with random it will coose 1 random number from the list deck
                # random_card = random.choice(deck)
                # # and then it will add the numbers to the list hand
                random_card = deck [0]
                hand.append(random_card)
                if random_card in deck:
                    deck.remove(random_card)
                    # in this loop i'm filtering out the choosen card from the deck

            hands[i] = hand
            # while in the loop "i" symbolizes a player
        # print hands
        hands = [deck, hands, players_name, num_of_players]
        return hands
# Class "Shuffled" is theclass where the game is drawing cards for each player

class Output(object):

    def top_card(self, game):
        c_top_card = game[3]
        color = game [8]
        if 'RED' == color:
            p_top_card = ('\033[1;31;48m' + "{0}".format(c_top_card[0]) + "\x1b[0m ")
        if 'GREEN' == color:
            p_top_card = ('\033[1;32;48m' + "{0}".format(c_top_card[0]) + "\x1b[0m ")
        if 'YELLOW' == color:
            p_top_card = ('\033[1;33;48m' + "{0}".format(c_top_card[0]) + "\x1b[0m ")
        if 'BLUE' == color:
            p_top_card = ('\033[1;34;48m' + "{0}".format(c_top_card[0]) + "\x1b[0m ")
        if 'RGYB' == color:
            p_top_card = ('\033[1;35;48m' + "{0}".format(c_top_card[0]) + "\x1b[0m ")
        print "Top card is: {0}".format(p_top_card)

    def player_hand(self, game):
        hands = game[6]
        turn = game [7]
        cards = game [13]
        hand = hands[turn]
        players_name = game[4]
        name_of_player = players_name[turn]
        print "{0}".format(name_of_player) + "'s cards are: "
        for num_of_card in range(len(hand)):
            card = hand[num_of_card]
            card = cards[card]
            if 'RED' in card:
                print num_of_card, ('\033[1;31;48m' + "{0}".format(card[0]) + "\x1b[0m ")
            if 'GREEN' in card:
                print num_of_card, ('\033[1;32;48m' + "{0}".format(card[0]) + "\x1b[0m ")
            if 'YELLOW' in card:
                print num_of_card, ('\033[1;33;48m' + "{0}".format(card[0]) + "\x1b[0m ")
            if 'BLUE' in card:
                print num_of_card, ('\033[1;34;48m' + "{0}".format(card[0]) + "\x1b[0m ")
            if 'RGYB' in card:
                print num_of_card, ('\033[1;35;48m' + "{0}".format(card[0]) + "\x1b[0m ")

    def ask_for_card(self, game):
        true = True
        while (true):
            try:
                choice = input("Enter number of card or 99 to draw a card from the deck: ")
            except NameError:
                continue
                # if the input is a letter it will raise a name error and ask again for number of players
                # it will ask for a number as long as the input is not a number
            except SyntaxError:
                continue
            except IndexError:
                continue
            else:
                break
        game [10] = choice

        return game

    def ask_for_plus3(self, game):
        choice = input("Draw a +3 or enter 99 to draw from cards deck")
        game [10] = choice
        return choice

    def ask_for__taki_card(self, game):
        choice = input("Enter card from the color or 99 to drew from the deck")
        game [10] = choice
        return game

    def ask_for_color(self, game):
        true = True
        print "1-RED 2-GREEN 3-YELLOW 4-BLUE"
        color = input("Choose a color: ")
        while color > 4:
            while (true):
                try:
                    print "1-RED 2-GREEN 3-YELLOW 4-BLUE"
                    color = input("Choose a color: ")
                except NameError:
                    continue
                except SyntaxError:
                    continue
                except IndexError:
                    continue
                else:
                    break
        if color == 1:
            color = "RED"
        if color == 2:
            color = "GREEN"
        if color == 3:
            color = "YELLOW"
        if color == 4:
            color = "BLUE"
        game [8] = color
        return game

    def stop(self):
        print "You have been stoped"

    def change(self):
        print "The turns have changed order"
# Class "Output" has a fuction for each print the game may need
# such as pring the players hand or print the top card

class Rules (Players):

    def colorandform(self, game):
        c_chosen_card = game[12]
        c_top_card= game[3]
        color = game [8]
        if c_chosen_card[1] == color: # same color
            rule = 2
        elif c_chosen_card[0] == c_top_card[0]: # same shape
            rule = 3
        elif c_chosen_card[1] == 'RGYB': # supr cards
            rule = 4
        else:
            rule = 1 # pull card from the deck
        game [14] = rule
        return game

    def evaloation_rule(self, game):
        choice = game[10]
        if choice == 99:
            Rules().pull_card(game)
        else:
            Rules().colored_chosen_card(game)
            Rules().colorandform(game)
            rule = game[14]
            if rule == 1:  # draw card from the deck
                Rules().pull_card(game)
            if rule == 2:  # same color cards
                Rules().same_color(game)
                Rules().action_cards(game)
                choice = game [10]
                if not choice == 99:
                    Rules().change_top_card(game)
            if rule == 3:  # same shape cards
                Rules().action_cards(game)
                if not choice == 99:
                    Rules().change_top_card(game)
            if rule == 4:  # super cards
                Rules().super_card(game)
                if not choice == 99:
                    Rules().change_top_card(game)

    def same_color(self, game):
        chosen_card = game[11]
        c_top_card = game[3]
        c_chosen_card = game [11]
        color = c_top_card[1]
        game[8] = color
        return game

    def super_card(self, game):
        c_top_card = game[3]
        hands = game[6]
        turn = game [7]
        hand = hands [turn]
        color = game [8]
        choice = game [10]
        chosen_card = game [11]
        c_chosen_card = game[12]
        hand.remove(chosen_card)
        superCards = ('Super Taki', 'Change Color', 'Stop', 'Plus', 'Switch', 'Taki')
        if c_chosen_card[0] == 'Change Color':
            Output().ask_for_color(game)
        if c_chosen_card[0] == 'Super Taki':
                color = Output().ask_for_color(game)
                while not choice == 99:
                    Output().player_hand(game)
                    Output().ask_for__taki_card(game)
                    choice = game[10]
                    tries = 0
                    if not choice == 99:
                        Rules().colored_chosen_card(game)
                        Rules().colorandform(game)
                        rule = game[14]
                        if rule == 2:  # same color
                            Rules().change_top_card(game)
                        else:
                            while tries > 5:
                                print "Wrong color"
                                print "You have", 5 - tries, "more times to try"
                                Output().ask_for__taki_card(game)
                                tries = tries + 1
                            else:
                                print "Wrong color"
                                Rules().pull_card(game)
                Rules().colored_top_card(game)
                c_top_card = game[3]
                if c_top_card in superCards:
                    Rules().next_turn(game)
                turn = Rules().next_turn(game)
        game [7] = turn
        return game

    def action_cards(self, game):
        deck = game[0]
        middle_deck = game[1]
        hands = game[6]
        turn = game[7]
        switch = game[9]
        choice = game[10]
        c_chosen_card = game[12]
        cards = game [13]
        superCards = ('Super Taki', 'Change Color', 'Stop', 'Plus', 'Switch', 'Taki')
        hand = hands[turn]
        if c_chosen_card[0] == 'Plus':
            Rules().change_top_card(game)
            Output().player_hand(game)
            Output().ask_for_card(game)
            Rules().colored_chosen_card(game)
            Rules().colorandform(game)
            rule = game[14]
            if rule == 2:  # same color
                Rules().change_top_card(game)
                Rules().action_cards(game)
            if rule == 3:
                Rules().change_top_card(game)
                Rules().action_cards(game)
                Rules().super_card(game)
            if rule == 4:
                Rules().pull_card(game)
        if c_chosen_card[0] == "+3":
            plusthree = 3
            while not choice == 99:
                Rules().next_turn(game)
                Output().player_hand(game)
                Output().ask_for_plus3(game)
                choice = game [10]
                if choice == 99:
                    for num_plus in range(plusthree):
                        card = deck[0]
                        hand.append(card)
                        deck.remove(card)
                    # Rules().next_turn(game)
                else:
                    Rules().colored_chosen_card(game)
                    Rules().colorandform(game)
                    rule = game [14]
                    if rule == 14:
                        Rules().change_top_card(game)
                        plusthree = plusthree + 3
                    else:
                        for num_plus in range(plusthree):
                            card = deck[0]
                            hand.append(card)
                            deck.remove(card)
                    game [15] = plusthree
                    hands [turn] = hand
                    game [6] = hands

        if c_chosen_card[0] == 'Switch':
            switch = switch * -1

        if c_chosen_card[0] == 'Taki':
            while not choice == 99:
                Rules().change_top_card(game)
                Output().player_hand(game)
                Output().ask_for__taki_card(game)
                choice = game[10]
                tries = 0
                if not choice == 99:
                    Rules().colored_chosen_card(game)
                    Rules().colorandform(game)
                    rule = game [14]
                    if rule == 2 : #same color
                        Rules().change_top_card(game)

                    else:
                        while tries >5:
                            print "Wrong color"
                            print "You have", 5-tries, "more times to try"
                            Output().ask_for__taki_card(game)
                            tries = tries + 1
                        else:
                            print "Wrong color"
                            Rules().pull_card(game)
            Rules().colored_top_card(game)
            c_top_card = game [3]
            if c_top_card[0] in superCards:
                Rules().next_turn(game)
                Rules().action_cards(game)
                Rules().super_card(game)

        if c_chosen_card[0] == 'Stop':

            Output().stop()
            Rules().next_turn(game)
        game[0] = deck
        game[1] = middle_deck
        hands[turn] = hand
        game[6] = hands
        game[7] = turn
        game [9] = switch
        game[10] = choice
        game[12] = c_chosen_card
        return game

    def change_top_card(self, game):
        middle_deck = game[1]
        hands = game[6]
        turn = game[7]
        choice = game [10]
        hand = hands[turn]
        chosen_card = game[11]
        hand.pop(choice)
        top_card = chosen_card
        middle_deck.append(top_card)
        hands [turn] = hand
        game[1] = middle_deck
        game[3] = top_card
        game [8] = hands
        return game

    def colored_top_card(self, game):
        color = game[8]
        cards = game[13]
        middle_deck = game[1]
        top_card = middle_deck[-1]
        c_top_card = cards[top_card]
        if not c_top_card[1] == 'RGYB':
            color = c_top_card[1]
        game[3] = c_top_card
        game [8] = color
        return  game

    def colored_chosen_card(self, game):
        hands = game [6]
        turn = game [7]
        hand = hands [turn]
        cards = game [13]
        choice = game [10]
        game [11] = chosen_card = hand[choice]
        game [12] = c_chosen_card = cards [chosen_card]
        return game

    def next_turn (self, game):
        turn = game[7]
        switch = game [9]
        num_of_players = game[5]
        if switch == 1:
            if turn < num_of_players:
                turn = turn + 1
            if turn == num_of_players:
                turn = 0
        if switch == -1:
            if turn == 0:
                turn = num_of_players
            if turn <= num_of_players:
                turn = turn - 1

        game [7] = turn
        game [9] = switch
        return game

    def pull_card (self, game):
        deck = game [0]
        hands = game [6]
        turn = game [7]
        hand = hands[turn]
        pull = deck[0]
        deck.remove(pull)
        hand.append(pull)
        hands [turn] = hand
        game [0] = deck
        game [6] = hands
        return game

    def pull_top_card(self, game):

        deck = game[0]
        middle_deck = game[1]
        top_card = deck [0]
        cards = game[13]
        deck.remove(top_card)
        middle_deck = []
        middle_deck.append(top_card)
        superCards = ('Super Taki', 'Change Color', 'Stop', 'Plus', 'Switch', 'Taki')
        c_top_card = cards[top_card]
        while c_top_card[0] in superCards:
            top_card = deck[0]
            deck.remove(top_card)
            middle_deck.append(top_card)
            c_top_card = cards[top_card]
        game [0] = deck
        game [1] = middle_deck
        return game
    # def taki (game):
# Class "Rules" has a function for each action or rule the may use or do
# such as draw a card for the player or ask for another card from the player

class Master (object):
    def __init__(self):
        cards = Cardsdeck()
        cards = cards.deck_of_cards()
        hands = Players().how_many_players()
        shuffle = Shuffled().draw_to_players(hands)
        deck = shuffle[0]
        players_hands = shuffle[1]
        players_names = shuffle[2]
        num_of_players = shuffle[3]
        turn = 0
        switch = 1
        game = [deck, 1, 2, 3, players_names, num_of_players, players_hands, turn, 8, switch,10 , 11, 12, cards, 14]
        Rules().pull_top_card(game)
        while num_of_players > 1:
            Rules().colored_top_card(game)
            Output().top_card(game)
            Output().player_hand(game)
            Output().ask_for_card(game)
            Rules().evaloation_rule(game)
            Rules().next_turn(game)
# Class "Master" isthe class where al the other class meet
# In class Master, the game is calling for the functions from the class and using them to advance the game

game = Master()
