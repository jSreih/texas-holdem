import random
class Poker():
  n = 2
  def __init__(self, n=2):
    if n == 2:
      self._players = Poker.n
    else:
      self._Players = n 
    self._Hands = []
    for i in range(0, n):
      hand = []
      self._Hands.append(hand)
    self._TableCards = []
    self._CardValue = {"2D":2, "3D":3, "4D":4, "5D":5, "6D":6, "7D":7, "8D":8, "9D":9, "10D":10, "JD":11, "QD":12, "KD":13, "AD":14 ,"2C":2, "3C":3, "4C":4, "5C":5, "6C":6, "7C":7, "8C":8, "9C":9, "10C":10, "JC":11, "QC":12, "KC":13, "AC":14 ,"2S":2, "3S":3, "4S":4, "5S":5, "6S":6, "7S":7, "8S":8, "9S":9, "10S":10, "JS":11, "QS":12, "KS":13, "AS":14 ,"2H":2, "3H":3, "4H":4, "5H":5, "6H":6, "7H":7, "8H":8, "9H":9, "10H":10, "JH":11, "QH":12, "KH":13, "AH": 14}
    self._Deck = list(self._CardValue.keys())
    random.shuffle(self._Deck)
    
  def add_card(self, p):
    '''Adds a card to the specefied player (p is the index of that player)'''
    self._Hands[p].append(self._Deck[0])
    self._Deck.pop(0)
    return self._Hands

  def add_to_table(self):
    '''Adds a card to the table'''
    self._TableCards.append(self._Deck[0])
    self._Deck.pop(0)
    return self._TableCards

  def IsStraightFlush(self, p):
    '''Checks each players hand to see if they got a straight(consecutive numbers one after another) and a flush (all cards with the same suit). ---> returns a bool value'''
    IsFlush = False
    IsStraight = False
    IsStraightFlush = False 
    list_check_straight = []
    list_check_flush = []
    count = 0
    
    # Checks to see if the player has a straight
    # Replaces the keys with the values of each card, making it easier to find which ones are the same (Ignores the suits) 
    for i in self._Hands[p]:
      list_check_straight.append(self._CardValue[i])
    list_check_straight.sort()
      # Because the ace is valued at 14, this exception needs to be made to count a straight going from Ace to 5 
    if (2 in list_check_straight) and (3 in list_check_straight) and (4 in list_check_straight) and (5 in list_check_straight) and (14 in list_check_straight): 
      IsStraight = True
      
    else:
      for i in range(0, len(list_check_straight)):
        # The index would be out of range if it were to loop on the on the last one
        if list_check_straight[i] == list_check_straight[len(list_check_straight)-1]:
          break
        elif list_check_straight[i] == list_check_straight[i+1] - 1:
          count += 1 
          if count == 5:
            IsStraight = True
            break
        else:
          count = 0
    # Checks to see if the player has a flush
    if IsStraight == True:
      IsFlush = False
      for i in self._Hands[p]:
        list_check_flush.append(i[1])
      for i in list_check_flush:
        if list_check_flush.count(i) >= 5:
          IsFlush = True
          break
          
    # If the player has both, then he has a straight flush
    if IsFlush == True and IsStraight == True:
      IsStraightFlush = True
    return IsStraightFlush
   
  def IsFourofaKind(self, p):
    '''Checks to see if a number appear 4 times ---> returns a bool value '''
    IsFourofaKind = False
    list_check = []
    # Replaces the keys with the values of each card, making it easier to find which ones are the same (Ignores the suits) 
    for i in self._Hands[p]:
      list_check.append(self._CardValue[i])

      
    for i in list_check:
      if list_check.count(i) == 4:
        IsFourofaKind = True
        break
    return IsFourofaKind

  def IsFullHouse(self, p):
    '''Checks to see if a number appear 3 times and another number appear 2 times. ---> returns a bool value'''
    IsFullHouse = False
    list_check = []
    # Replaces the keys with the values of each card, making it easier to find which ones are the same (Ignores the suits) 
    for i in self._Hands[p]:
      list_check.append(self._CardValue[i])

    
    for x in list_check:
      if list_check.count(x) == 3:
        for y in list_check:
          if (list_check.count(y) == 2) and (y != x):
            IsFullHouse = True
            break
            
    return IsFullHouse

  def IsFlush(self, p):
    '''Checks to see if all the cards are the same suit ---> returns a bool value'''
    IsFlush = False
    list_check_flush = []
  
    for i in self._Hands[p]:
      list_check_flush.append(i[1])

    for i in list_check_flush:
      if list_check_flush.count(i) >= 5:
        IsFlush = True
        break
      
    return IsFlush

  def IsStraight(self, p):
    '''Checks to see if the player has a straight (consecutive numbers one after another). ---> returns a bool value'''
    IsStraight = False
    list_check_straight = []
    count = 0

    
    for i in self._Hands[p]:
      list_check_straight.append(self._CardValue[i])
    list_check_straight.sort()



    if (2 in list_check_straight) and (3 in list_check_straight) and (4 in list_check_straight) and (5 in list_check_straight) and (14 in list_check_straight): 
      IsStraight = True
    else:
      for i in range(0, len(list_check_straight)):
        
        if list_check_straight[i] == list_check_straight[len(list_check_straight)-1]:  
          break

          
        elif list_check_straight[i] == list_check_straight[i+1] - 1:
          count += 1 
          if count == 5:
            IsStraight = True
            break
            
        else: 
          count = 0
    return IsStraight

  def IsThreeofaKind(self, p):
    '''Checks to see if the player has a number 3 times. ---> returns a bool value'''
    IsThreeofaKind = False
    list_check = []
    # Replaces the keys with the values of each card, making it easier to find which ones are the same (Ignores the suits) 
    for i in self._Hands[p]:
      list_check.append(self._CardValue[i])  
      
    for i in list_check:
      if list_check.count(i) == 3:
        IsThreeofaKind = True 
        break
    return IsThreeofaKind
        
  
  def IsTwoPairs(self, p):
    '''Checks to see if the player has a number 2 times. ---> returns a bool value'''
    IsTwoPairs = False
    list_check = []
    # Replaces the keys with the values of each card, making it easier to find which ones are the same (Ignores the suits) 
    for i in self._Hands[p]:
      list_check.append(self._CardValue[i]) 
      
    for x in list_check:
      if list_check.count(x) == 2:
        for y in list_check:
          if list_check.count(y) == 2 and x != y:
            IsTwoPairs = True 
        break
    return IsTwoPairs

  def IsOnePair(self,p):
    IsPair = False
    list_check = []
    # Replaces the keys with the values of each card, making it easier to find which ones are the same (Ignores the suits) 
    for i in self._Hands[p]:
      list_check.append(self._CardValue[i])  
      
    for i in list_check:
      if list_check.count(i) == 2:
        IsPair = True 
        break
    return IsPair

  def HighCard(self, p):
    '''Returns the Highest card a player has ---> returns an bool value'''
    return True


class TexasHoldem(Poker):
  def __init__(self, n):
    super().__init__(n)

  def deal(self):
    '''Deals out the cards to the players and lays out 5 cards on the table. ---> list value'''
    for i in range(0, self._Players):
      Poker.add_card(self, i)
      Poker.add_card(self, i)
    for i in range(0, 5):
      Poker.add_to_table(self)
    return f'''Here are the hands of each player {self._Hands}.
Here are the cards on the table {self._TableCards}
'''

  def hands(self):
    '''Looks at the 2 cards each player has and then finds the best possible hand that person can get with the 5 cards on the table ---> returns a string'''
    for p in range(0, self._Players):
      for i in range(0, 5):
        self._Hands[p].append(self._TableCards[i]) # Combines the cards that players has and the cards on the table
      if Poker.IsStraightFlush(self, p) == True:
        print("Player", p+1, "has a Straight Flush")
      elif Poker.IsFourofaKind(self, p) == True:
        print("Player", p+1, "has a Four of a Kind")
      elif Poker.IsFullHouse(self, p) == True:
        print("Player", p+1, "has a Full House")
      elif Poker.IsFlush(self, p) == True:
        print("Player", p+1, "has a Flush")
      elif Poker.IsStraight(self, p) == True:
        print("Player", p+1, "has a Straight")
      elif Poker.IsThreeofaKind(self, p) == True:
        print("Player", p+1, "has a Three of a Kind")
      elif Poker.IsTwoPairs(self, p) == True:
        print("Player", p+1, "has Two Pairs")
      elif Poker.IsOnePair(self, p) == True:
        print("Player", p+1, "has a Pair")
      else:
        print("Player", p+1, "has a High Card.")
    return self._Hands


game = TexasHoldem(10)
print(game.deal())
game.hands()