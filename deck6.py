import random
class Deck :
    def __init__ (self):
        self.symbol = ["♣","♦","♥","♠"]
        self.point = ["1","2","3","4","5","6","7","8","9","A","J","K","Q"]
        self.box = []
        for i in self.symbol:
            for j in self.point:
                self.box.append(i + j)
    
    def shuffle_card(self):
        random.shuffle(self.box)
        return self.box

class Dealer : 
    def __init__(self,deck):
        self.dealer_deck = deck
        print(self.dealer_deck)

    def give_cards(self):
        self.give_card = [self.dealer_deck[0] , self.dealer_deck[1]]
        self.remove_cards = [self.dealer_deck.pop(0) , self.dealer_deck.pop(0)]
        return self.give_card
    
    def give_player_hit(self):
        self.draw_card = self.dealer_deck[0]
        self.remove_draw_cards = self.dealer_deck.pop(0)
        return self.draw_card
    
class Player :
    def __init__(self,cards,player_name):
        self.player_cards = cards
        self.player_name = player_name

    def show_player_cards(self):
        print(self.player_name,self.player_cards)

    def player_hit_stand(self,response):
        self.player_response = response
        if self.player_response == "H":
            self.player_cards.append(dealer.give_player_hit())
        elif self.player_response == "S" :
            pass
        print(self.player_name,self.player_cards)

    def player_check_point(self):
        self.player_point = []
        self.sum = 0

        for l in self.player_cards :
            self.player_point.append(l[1:2])
        
        for sum_score in self.player_point :
            if sum_score == "K":
               sum_score = 10
            if sum_score == "J":
                sum_score = 10
            if sum_score == "Q":
                sum_score = 10
            if sum_score == "A":
                c = int(input("You want A be 1 or 11 : "))
                sum_score = c
            sum_score = int(sum_score) + self.sum
            self.sum = int(sum_score)

    def score(self):
        return self.sum

    def player_show_score(self):
        print(self.player_name,"Point =",self.sum)
        if self.sum > 21:
            print(self.player_name,"you are burst")

    def check_bus(self):
        if self.sum > 21:
            return True

class Blackjack():
    def start_game(self,player):
        player_response = ""
        while player_response != "S":
            player.show_player_cards()
            player_response = input("Hit or Stand (H/S) : ")
            player.player_hit_stand(player_response)
            player.player_check_point()
            player.player_show_score()
            if player.check_bus() == True :
                break

    def announce(self,player_1,player_2):
        if player_1.score() > 21 and player_2.score() > 21:
            print("You all Draw")
        if player_1.score() == player_2.score():
            print("You all Draw")
        elif player_1.score() > player_2.score() and player_1.score() <= 21:
            print("Player1 Win")
        elif player_1.score() < 21 and player_2.score() > 21 :
            print("Player1 Win")
        elif player_1.score() == 21 :
            print("Player1 BlackJack!!!")
        elif player_2.score() > player_1.score() and player_2.score() <= 21:
            print("Player2 Win")
        elif player_2.score() <= 21 and player_1.score() > 21 :
            print("Player2 Win")
        elif player_2.score() == 21 :
            print("Player2 BlackJack!!!")
        elif player_1.score == 21 and player_2.score() == 21 :
            print("You all BlackJack!!!")

deck = Deck()
deck.shuffle_card()

dealer = Dealer(deck.shuffle_card())

player1 = Player(dealer.give_cards(),"Player1")
player2 = Player(dealer.give_cards(),"Player2")

blackjack = Blackjack()
blackjack.start_game(player1)
blackjack.start_game(player2)
blackjack.announce(player1,player2)