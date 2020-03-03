import Dominion
import unittest
import random
from collections import defaultdict
import io
import sys
import pytest


"""
**************************************************************************************************************************************************************
Globally defining variables that will be used in the test suite
**************************************************************************************************************************************************************
"""
#Get player names
player_names = ["Sonia","*Owen"]

#number of curses and victory cards
if len(player_names)>2:
    nV=12
else:
    nV=8
nC = -10 + 10 * len(player_names)

#Define box
box = {}
box["Woodcutter"]=[Dominion.Woodcutter()]*10
box["Smithy"]=[Dominion.Smithy()]*10
box["Laboratory"]=[Dominion.Laboratory()]*10
box["Village"]=[Dominion.Village()]*10
box["Festival"]=[Dominion.Festival()]*10
box["Market"]=[Dominion.Market()]*10
box["Chancellor"]=[Dominion.Chancellor()]*10
box["Workshop"]=[Dominion.Workshop()]*10
box["Moneylender"]=[Dominion.Moneylender()]*10
box["Chapel"]=[Dominion.Chapel()]*10
box["Cellar"]=[Dominion.Cellar()]*10
box["Remodel"]=[Dominion.Remodel()]*10
box["Adventurer"]=[Dominion.Adventurer()]*10
box["Feast"]=[Dominion.Feast()]*10
box["Mine"]=[Dominion.Mine()]*10
box["Library"]=[Dominion.Library()]*10
box["Gardens"]=[Dominion.Gardens()]*nV
box["Moat"]=[Dominion.Moat()]*10
box["Council Room"]= [Dominion.CouncilRoom()] * 10
box["Witch"]=[Dominion.Witch()]*10
box["Bureaucrat"]=[Dominion.Bureaucrat()]*10
box["Militia"]=[Dominion.Militia()]*10
box["Spy"]=[Dominion.Spy()]*10
box["Thief"]=[Dominion.Thief()]*10
box["Throne Room"]= [Dominion.ThroneRoom()] * 10

supply_order = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                6:['Gold','Adventurer'],8:['Province']}

#Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)
random10 = boxlist[:10]
supply = defaultdict(list,[(k,box[k]) for k in random10])


#The supply always has these cards
supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
supply["Silver"]=[Dominion.Silver()]*40
supply["Gold"]=[Dominion.Gold()]*30
supply["Estate"]=[Dominion.Estate()]*nV
supply["Duchy"]=[Dominion.Duchy()]*nV
supply["Province"]=[Dominion.Province()]*nV
supply["Curse"]=[Dominion.Curse()]*nC

#initialize the trash
trash = []

#function from Dominion.py in order to show the proper name of card in discard pile
def namesinlist(cardlist):
    namelist = []    
    for c in cardlist:
        namelist.append(c.name)
    return namelist

#Costruct the Player objects
players = []
for name in player_names:
    if name[0]=="*":
        players.append(Dominion.ComputerPlayer(name[1:]))
    elif name[0]=="^":
        players.append(Dominion.TablePlayer(name[1:]))
    else:
        players.append(Dominion.Player(name))

# for value in supply_order:
#     print ("COST: ",value)
#     for stack in supply_order[value]:
#         if stack in supply:
#             print (stack, len(supply[stack]))
#     print("\n")

initial_hand = players[0].hand.copy()

"""
**************************************************************************************************************************************************************
Global variable are defined
**************************************************************************************************************************************************************
"""


class TestTotalBuyPower(unittest.TestCase):
    def test_add_gold(self):
        #print("totalbuypower test_add_gold...")
        #print(players[0].hand)
        bp1 = Dominion.totalbuypower(players[0].hand)
        #print(bp1)
        players[0].hand.append(supply["Gold"][0])
        #print(players[0].hand)
        bp2 = Dominion.totalbuypower(players[0].hand)
        #print(bp2)
        self.assertEqual(bp1 + 3, bp2)

    def test_add_festival(self):
        #print("totalbuypower test_add_festival...")
        #print(players[0].hand)
        bp1 = Dominion.totalbuypower(players[0].hand)
        #print(bp1)
        supply["Festival"]=[Dominion.Festival()]*1
        players[0].hand.append(supply['Festival'][0])
        #print(players[0].hand)
        bp2 = Dominion.totalbuypower(players[0].hand)
        #print(bp2)
        self.assertEqual(bp1 + 2, bp2)

    def test_remove_cards(self):
        #print("totalbuypower test_remove_cards...")
        #print(players[0].hand)
        bp1 = Dominion.totalbuypower(players[0].hand)
        #print(bp1)
        temp_hand = players[0].hand.copy()
        players[0].hand = []
        #print(players[0].hand)
        bp2 = Dominion.totalbuypower(players[0].hand)
        #print(bp2)
        self.assertNotEqual(bp1, 0)
        self.assertEqual(0, bp2)
        players[0].hand = temp_hand

    def test_basic_count(self):
        #print("totalbuypower test_basic_count...")
        #print(players[0].hand)
        bp1 = 0
        for card in initial_hand:
            if card.name == "Copper":
                bp1+=1
        #print(bp1)
        bp2 = Dominion.totalbuypower(initial_hand)
        #print(bp2)
        self.assertEqual(bp1, bp2)

    def test_add_province(self):
        #print("totalbuypower test_add_province...")
        #print(players[0].hand)
        bp1 = Dominion.totalbuypower(players[0].hand)
        #print(bp1)
        players[0].hand.append(supply["Province"][0])
        #print(players[0].hand)
        bp2 = Dominion.totalbuypower(players[0].hand)
        #print(bp2)
        self.assertEqual(bp1, bp2)

class TestWitchPlay(unittest.TestCase):
    Dominion.Witch().play(players[0], players, supply, trash)
    #print("initial VP: ", players[1].calcpoints())
    def test_place_curse(self):
        #print("play test_place_curse...")
        for player in players:
            #print(player.discard)
            if player is not players[0]:
                self.assertEqual(len(player.discard), 1)

    def test_self_curse(self):
        #print("play test_place_curse...")
        #print(players[0].discard)
        self.assertEqual(len(players[0].discard), 0)

    def test_new_vp(self):
        #print("play test_new_vp...")
        #print("cursed VP: ", players[1].calcpoints())
        self.assertGreater(players[0].calcpoints(), players[1].calcpoints())

    def test_no_curse(self):
        #print("play test_no_curse...")
        before_length = len(players[1].discard)
        #print(players[1].discard)
        while len(supply["Curse"]) > 0:
            supply["Curse"].pop()
        Dominion.Witch().play(players[0], players, supply, trash)
        #print(players[1].discard)
        after_length = len(players[1].discard)
        self.assertEqual(before_length, after_length)

    def test_protect(self):
        #print("play test_protect...")
        dis1 = len(players[1].discard)
        #print(players[1].discard)
        supply["Curse"] = [Dominion.Curse()] * 1
        supply["Moat"] = [Dominion.Moat()] * 1
        players[1].hand.append(supply['Moat'][0])
        Dominion.Witch().play(players[0], players, supply, trash)
        #print(players[1].discard)
        dis2 = len(players[1].discard)
        self.assertEqual(dis1, dis2)


if __name__ == '__main__':
    print("=====\nTesting\n=====")
    unittest.main()




