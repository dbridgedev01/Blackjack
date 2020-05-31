import random


def all_cards():
    """
    returns A DECK IN THE FORMAT [(suitname,card)]
    """
    suits = ['Clubs','Diamonds','Hearts','Spades']
    uCardset = []
    for item in suits:
        uCardset.append(("ACE",item))
        for num in range(2,11):
            uCardset.append((num,item))
        uCardset.append(("JACK",item))
        uCardset.append(("QUEEN",item))
        uCardset.append(("KING",item))  
    return uCardset

class Start:
    """
    Class To Begin With Name And Amount Of Bet For The Players
    """
    def __init__(self,name,betMoney):
        self.name = name
        self.betMoney = betMoney
        self.totalMoney = 0
        self.cardsInHand = []
        self.cardValue = 0
        self.nextcall = "" #FOR SAYING THERE'S NO BUST OR DIRECT WIN
    
    def set_player_cards(self,uCards):
        """"
        Giving ONE Card To The Player
        """
        last = len(uCards)
        self.cardsInHand.append(uCards[last-1])
        uCards.pop()
        return uCards
    def player_print_all(self):
        """
        TO PRINT THE PLAYER'S CARDS IN HAND
        """
        print(f"{self.name} <> Cards : ")
        for a,b in self.cardsInHand:
             print(f"{a} Of {b}")
        print("\n\n")
    
    
    def set_in_hand_value(self,lst):
        self.cardValue = 0
        """
        TAKES IN A 2-D list with an ordered tuple to assign values and check
        """
        for check,other in lst:
            if(isinstance(check,int)):
                self.cardValue += check
            elif(check == "ACE"):
                aceValue = int(input(f"{self.name} <> YOU'VE GOT AN ACE <> DO YOU WANT IT TO BE A 1 OR 11?\n[YOU CAN CHANGE IT LATER : "))
                if(aceValue==11):
                    self.cardValue += 11
                else:
                    self.cardValue += 1
            else:
                self.cardValue +=10
    
    def check_win(self):
        """
        Checks for a bust or direct winner
        """
        if(self.cardValue>21):
            return "BUST"   
        elif(self.cardValue == 21):
            return "WIN"
        else:
            return "OTHERWISE"



    


#Dealer Class
class Dealer:
    """
    Creating the only instance of the dealer
    """
    def __init__(self,dealerMoney=100000000,dealerName = "dBridgedDev"):
        self.dealerMoney = dealerMoney
        self.dealerName = dealerName
        self.cardsInHand = []
        self.cardValue = 0
    
    def set_dealer_cards(self,uCards):
        """"
        Giving ONE Card To The Dealer
        """ 
        last = len(uCards)
        self.cardsInHand.append(uCards[last-1])
        uCards.pop()
        return uCards
    
    def dealer_print(self):
        """
        First Print Of Dealer's Cards
        """
        print(f"\n\nDealer For The Day : {self.dealerName}")
        print("Dealer's Cards <>")
        print(f"{self.cardsInHand[0][0]} Of {self.cardsInHand[0][1]} &&")
        print("CARD : XXXX\n\n")
    
    def delear_final_print(self):
        """
        TO PRINT THE DEALER'S CARDS IN HAND
        """
        print(f"{self.dealerName} <> Cards : ")
        for a,b in self.cardsInHand:
             print(f"{a} Of {b}")
        print("\n\n")
    
    def dealer_in_hand_value(self,lst):
        self.cardValue = 0
        """
        TAKES IN A 2-D list with an ordered tuple to assign values and check
        """
        for check,other in lst:
            if(isinstance(check,int)):
                self.cardValue += check
            elif(check == "ACE"):
                aceValue = int(input(f"{self.dealerName} <> YOU'VE GOT AN ACE <> DO YOU WANT IT TO BE A 1 OR 11?\n[YOU CAN CHANGE IT LATER : "))
                if(aceValue==11):
                    self.cardValue += 11
                else:
                    self.cardValue += 1
            else:
                self.cardValue +=10
    def check_win_dealer(self):
        """
        Checks for a bust or direct winner
        """
        if(self.cardValue>21):
            return "BUST"   
        elif(self.cardValue == 21):
            return "WIN"
        else:
            return "OTHERWISE"






def allcall(players, playerCount=0):
    """
    PROCEDURAL THROUGHOUT FOR CHECKING BUST OR NOT
    returns a value if not for busting or winning
    """
    #FOR ALL PLAYERS
    if(playerCount>0):
        for i in range(playerCount):
            players[i].set_in_hand_value(players[i].cardsInHand)
            
            if (players[i].check_win() == "BUST"):
                print(f"{players[i].name} <> SORRY YOU'RE OUT!\nBETTER LUCK NEXT TIME!")
                print(f"YOUR CARD VALUE : {players[i].cardValue}")
                players.pop(i)
            elif (players[i].check_win() == "WIN"):
                print(f"{players[i].name} <> HEY YOU'VE WON 1.5 * YOUR BET!")
                print(f"YOUR CURRENT BALANCE : {players[i].betMoney * 1.5} SEE YOU AT THE NEXT ROUND! ")
                print(f"YOUR CARD VALUE : {players[i].cardValue}")
                players.pop(i)
            else:
                players[i].nextcall = "PROCEED"
    #FOR SINGLE PLAYER
    else:
        players.set_in_hand_value(players.cardsInHand)
            
        if (players.check_win() == "BUST"):
            print(f"{players.name} <> SORRY YOU'RE OUT!\nBETTER LUCK NEXT TIME!")
            print(f"YOUR CARD VALUE : {players.cardValue}")
            players.nextcall = "OUT"
        elif (players.check_win() == "WIN"):
            print(f"{players.name} <> HEY YOU'VE WON 1.5 * YOUR BET!")
            print(f"YOUR CURRENT BALANCE : {players.betMoney * 1.5} SEE YOU AT THE NEXT ROUND! ")
            print(f"YOUR CARD VALUE : {players.cardValue}")
            players.nextcall = "OUT"
        else:
            players.nextcall = "PROCEED"




#MAIN FUNCTION


print("Welcome TO Blackjack!\n")
playerCount = int(input("\nEnter The Number Of Players : "))

players = [] #List Of All The Players, Empty At First

for i in range(playerCount):
    playerName = input(f"\nEnter The Name Of Player {i+1} : ")
    betMoney = int(input(f"\n{playerName} >< Enter Your Bet Money : "))
    players.append(Start(playerName,betMoney))
    

uCardSet = all_cards() #Universal Card Set

for i in range(2): #Shuffle Twice 
    random.shuffle(uCardSet)

mainDealer = Dealer()
j=0 # TO RUN THE LOOP TWICE
while (j!=2):
    uCardSet = mainDealer.set_dealer_cards(uCardSet) #DEALER GETS THE CARD

    for i in range(playerCount):
        uCardSet = players[i].set_player_cards(uCardSet) #PLAYER GETS CARD
    j=j+1

mainDealer.dealer_print()

for i in range(playerCount):
    players[i].player_print_all()

#SET VALUES TO ALL CARDS AND SEE IF THERE'S A WINNER AT THE BEGINNING OR OTHERWISE

allcall(players,playerCount) #CHECK

#FOR DOING A HIT OR STAY AND GO ACROSS THE TABLE FOR ALL PLAYERS
for i in range(len(players)):
    if(players[i].nextcall == "PROCEED"):
        response = input(f"\n{players[i].name} >< Do You Want TO HIT OR STAY? : ")
        if(response.upper()=="STAY"):
            continue
        while(response.upper()=="HIT"):
            uCardSet = players[i].set_player_cards(uCardSet)
            players[i].player_print_all()
            allcall(players[i])
            if(players[i].nextcall == "OUT"):
                break
            response = input(f"\n{players[i].name} >< Do You Want TO HIT OR STAY? : ")

#CREATING A NEW LIST AND THROWING OUT ALL THE PLAYERS WHO BUSTED
finalplayers = []
for i in range(len(players)):
    if(players[i].nextcall == "OUT"):
        continue
    else:
        finalplayers.append(players[i])

#CHECKS IF THERE ARE PLAYERS OR NOT
if(len(finalplayers) == 0):
    print("NO MORE PLAYERS LEFT :/")

else:
    print("GOING AHEAD WITH THE ROUND!\nIN THE FINALS : \n")
    for i in range(len(finalplayers)):
        print(f"{i+1}.{finalplayers[i].name}!\n")

    print("TIME TO REVEAL THE DEALER'S CARDS!")
    mainDealer.delear_final_print()
    mainDealer.dealer_in_hand_value(mainDealer.cardsInHand)
    print(f"DEALER IN HAND VALUE! : {mainDealer.cardValue}\n")
    if(mainDealer.check_win_dealer() == "BUST"):
        print("DEALER BUSTED! ALL PLAYERS GET 2X THE BET AMOUNT")
        for i in range(len(finalplayers)):
            print(f"{finalplayers[i].name} <> YOUR FINAL AMOUNT : {finalplayers[i].betMoney*2} ")
    #DEALER HITS UNTIL HIS HAND BECOMES 17 OR HIGHER
    else:
        while(mainDealer.cardValue<17):
            uCardSet = mainDealer.set_dealer_cards(uCardSet)
            mainDealer.dealer_in_hand_value(mainDealer.cardsInHand)
        mainDealer.delear_final_print()
        print(f"DEALER IN HAND VALUE! : {mainDealer.cardValue}\n")
        
        if(mainDealer.check_win_dealer() == "BUST"):
            print("DEALER BUSTED! ALL PLAYERS GET 2X THE BET AMOUNT")
        
            for i in range(len(finalplayers)):
                print(f"{finalplayers[i].name} <> YOUR FINAL AMOUNT : {finalplayers[i].betMoney*2} ")
        else:
            for i in range(len(finalplayers)):
                if(finalplayers[i].cardValue>mainDealer.cardValue):
                    print(f"{finalplayers[i].name} >< YOU HAVE A HIGHER VALUE THAN THE DEALER! : {finalplayers[i].cardValue}")
                    print(f"{finalplayers[i].name} <> YOUR FINAL AMOUNT : {finalplayers[i].betMoney*2} ")
                else:
                    print(f"{finalplayers[i].name} >< SORRY YOU LOSE YOUR BET, YOUR CARD VALUE IS LOWER! : {finalplayers[i].cardValue}")
                    print("DEALER GETS YOUR MONEY :/")
print("\n\nTHANKS FOR PLAYING!")
print("A TEXT BASED BLACKJACK GAME BY @dBridgeDev")
