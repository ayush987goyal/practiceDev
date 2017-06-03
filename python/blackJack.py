import random

class deck(object):
	def __init__(self):
		self.cards = {'A':10,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

	def deal(self):	
		temp = random.randint(1,13)
		if(temp>1 and temp <11):
			return str(temp)
		else:
			if(temp==1): return "A"
			elif(temp==11): return "J"
			elif(temp==12): return "Q"	
			else: return "K"

	def getCardValue(self,yourCards):	
		cardSum=0
		check=False
		for card in yourCards:
			cardSum += self.cards[card]
			if(card=='A'): check=True
		
		if(check):
			if(cardSum > 21):
				return cardSum -10
		return cardSum

	def printCard(self,yourCard):
		print("|"+yourCard+"|")


class player(object):
	def __init__(self,money=100):
		self.money = money
		self.playerCards = []

	def addCard(self, card):
		self.playerCards.append(card)	

	def bet(self):
		amount = input("How much do you wanna bet? ")
		if(self.money >= amount):
			self.money -= amount
			print("Your bet: " + str(amount))
			return amount
		else:
			print("Invalid amount! Please try again")
			self.bet()

	def updateBalance(self,ifWon,amount):
		if(ifWon): self.money += amount
		else: self.money -= amount

mainDeck = deck()
#mainDeck.printCard(mainDeck.deal())

opponent = player()
dealer = player(100000)
#player1.bet()

playMore=True

print("Welcom to Black Jack")

while(playMore):
	betAmount = opponent.bet()
	print("Your cards: ")
	card1 = mainDeck.deal()
	card2 = mainDeck.deal()
	opponent.addCard(card1)
	opponent.addCard(card2)
	mainDeck.printCard(card1)
	mainDeck.printCard(card2)

	print("Dealer cards: ")
	card1 = mainDeck.deal()
        card2 = mainDeck.deal()
        dealer.addCard(card1)
        dealer.addCard(card2)
        mainDeck.printCard(card1)
        mainDeck.printCard(" ")

	choice = "h"
	while(choice != "s"):
		choice = raw_input("What's your move?hit-h or stand-s :")
		if(choice == "s"):
			continue
		else:
			card = mainDeck.deal()
			opponent.addCard(card)
			mainDeck.printCard(card)

	print("Dealer's move")
	mainDeck.printCard(card1)
	mainDeck.printCard(card2)		
	while(mainDeck.getCardValue(dealer.playerCards) < 17):
			card = mainDeck.deal()
                        dealer.addCard(card)
                        mainDeck.printCard(card)

	if(mainDeck.getCardValue(opponent.playerCards) > 21):	
		opponent.updateBalance(False,betAmount)
		print("Dealer won!")
	elif(mainDeck.getCardValue(dealer.playerCards) > 21):
		opponent.updateBalamce(True,betAmount*2)
		print("Player won!")
	elif(mainDeck.getCardValue(opponent.playerCards) > mainDeck.getCardValue(dealer.playerCards)):	
		opponent.updateBalamce(True,betAmount*2)
		print("Player won!")
	elif(mainDeck.getCardValue(opponent.playerCards) < mainDeck.getCardValue(dealer.playerCards)):
		opponent.updateBalance(False,betAmount)
                print("Dealer won!")
	else:
		print("Push!!")

	play = raw_input("Wanna play more? y/n :")
	if(play == "y"): playMore = True
	elif(play=="n"): playMore = False
	else:
		print("Invalid response! ending")
		playMore = False
