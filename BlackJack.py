import random
from IPython.display import clear_output
import os
def clear():
    os.system( 'cls' )


ranks=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack','Queen','King','Ace')
suits=('Hearts', 'Diamonds', 'Spades', 'Clubs')
values={'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10,'King':10,'Ace':11}
playing=True
class Cards():
	def __init__(self, rank, suit):
		self.suit=suit
		self.rank=rank
		self.cardValue=values[self.rank]
	def __repr__(self):
		return self.rank+' of '+self.suit

class Decks():
	## class used for creating a single deck used for the game
	def __init__(self):
		self.deck=[]
		for x in ranks:
			for y in suits:
				self.deck.append(Cards(x, y))
	def __str__(self):
		return str(self.deck)
	def shuffle(self):
		random.shuffle(self.deck)

class Hands():
	##class for both players and house's hand, initalises and keeps track of the value
	def __init__(self):
		self.cards=[]
		self.value=0
		self.aces=0
	def add_card(self, count): ##removes number of cards from deck and adds them to hand, also updates hand value
		for i in range(0,count):
			self.cards.append(playingDeck.deck.pop(-1))
			self.value+=self.cards[-1].cardValue
			if self.cards[-1].rank=='Ace':
				self.aces+=1
	def adjust_for_ace(self):
		if self.aces>0 and self.value>21:
			self.value-=10
			self.aces=0
	def __str__(self):
		return '\n'+str(self.cards)+' '+str(self.value)+'\n'
	 		
class Chips:
	##Players chips
	def __init__(self):
		self.total=100
		self.bet=0
	def take_bet(self):
		while True:
		##Checking for the correct input of int bet
			try:
				self.bet=int(input('You have {} chips available, place your bet\n'.format(self.total)))
			except ValueError:
				print ("You have to enter a number")
			else:
				if self.total>=self.bet:
					self.total-=self.bet
					break
				else:
					print("insufficient funds!")
	def win_bet(self):
		self.total+=self.bet*2
		print("congrats, you have won {}".format(chip.bet))
	def lose_bet(self):
		print("You have lost {}".format(chip.bet))


def yn_input(lines):
	while True:
		##Checking for the correct input of int bet
		try:
			yorn=input(lines +'\n Enter y or n\n')
		except ValueError:
				print ("You have to enter y or n\n")
		else:
			if yorn=='y':
				return True
			elif yorn=='n':
				return False
clear()
print('*****Welcome to the BlackJack Table, take a seat*****')

	
chip=Chips()

while playing:
	
	playingDeck=Decks()
	playingDeck.shuffle()
	playerHand=Hands()
	houseHand=Hands()
	playerHand.add_card(2)
	houseHand.add_card(2)
	clear()
	chip.take_bet()		
	while True:
		clear()
		playerHand.adjust_for_ace()
		print("---------------------------------------------------------------------\nHouse hand: \n {} \nPlayer hand: \n {} \n Your bet {} *********** remaining funds {}\n".format(houseHand.cards[0], playerHand, chip.bet, chip.total))
		if playerHand.value>21:
			print("Overeached")
			break
		if yn_input('Do you want to hit or continue'):
			playerHand.add_card(1)
			continue
		break
	playerHand.adjust_for_ace()
	if playerHand.value<=21:
		while houseHand.value<17:
			houseHand.add_card(1)
		if houseHand.value<=21:
			if houseHand.value>=playerHand.value:
				chip.lose_bet()
			else:
				chip.win_bet()
		else:
			chip.win_bet()
	else:
		chip.lose_bet()
	print("---------------------------------------------------------------------\nHouse hand: \n {} \nPlayer hand: \n {} \n Your bet {} *********** remaining funds {}\n".format(houseHand.cards[0], playerHand, chip.bet, chip.total))
	if chip.total<=0:
			print("See you next time")
			playing=False
			break
	
	playing=yn_input('Do you want to continue playing')



		


