# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:42:42 2015

@author: tfleck
"""
import sys
import Dominion
import random
import time
from collections import defaultdict


def print_action_cards():
    print('\n\n\n')
    print('\x1b[3;34;47m'+'**************************************'+'\x1b[0m')
    print('\x1b[3;34;47m'+'***********  ACTION CARDS  ***********'+'\x1b[0m')
    print('\n'"Woodcutter: +1 Buy and +$2")
    print('\n'"Smithy: +3 Cards")
    print('\n''\x1b[3;97;40m' + 'Laboratory: +2 Cards +1 Action' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Village: +1 Cards +2 Action' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Festival: +2 Actions, +1 Buy, and +$2.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Market: +1 card and +1 Action, +$1, and +1 Buy.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Chancellor: +$2, You may immediately put your deck into your discard pile.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Workshop: Gain a card costing up to $4.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Moneylender: You may trash a Copper from your hand for +$3.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Chapel: Trash up to 4 cards from your hand.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Cellar: +1 Action, Discard any number of cards, then draw that many.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Remodel: Trash a card from your hand. Gain a card costing up to $2 more than it.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Adventurer: Reveal cards from your deck until you reveal 2 Treasure cards. Put those Treasure cards into your hand and discard the other revealed cards.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Feast: Trash this card. Gain a card costing up to $5.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Mine: You may trash a Treasure from your hand. Gain a Treasure to your hand costing up to $3 more than it.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Library: Draw until you have 7 cards in hand, skipping any Action cards you choose to; set those aside, discarding them afterwards.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Moat: +2 Cards When another player plays an Attack card,  you may first reveal this from your hand, to be unaffected by it.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Council Room: +4 Cards +1 Buy Each other player draws a card.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Witch: +2 Cards Each other player gains a Curse.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Bureaucrat: Gain a Silver onto your deck.  Each other player reveals a Victory card from their hand and puts it onto their deck  (or reveals a hand with no Victory cards).' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Militia: +$2 Each other player discards down to 3 cards in hand.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Spy: +1 Card +1 Action Each player (including you) reveals the top card  of his deck and either discards it or puts it back, your choice.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Thief: Each other player reveals the top 2 cards of his deck.  If they revealed any Treasure cards, they trash one of them that you choose.  You may gain any or all of these trashed cards.  They discard the other revealed cards.' + '\x1b[0m')
    print('\n''\x1b[3;97;40m' + 'Throne Room: You may play an Action card from your hand twice.' + '\x1b[0m')
    print('\x1b[3;34;47m'+'**************************************'+'\x1b[0m')



print('\x1b[3;34;47m'+'***********************************************************'+'\x1b[0m')
print('\x1b[3;34;47m'+'******************* WELCOME TO DOMINION *******************'+'\x1b[0m')
print('\x1b[3;34;47m'+'***********************************************************'+'\x1b[0m')

print('\n\n\n')
print('\x1b[3;34;47m'+'**************************************'+'\x1b[0m')
print('\x1b[3;34;47m'+'***************  RULES  **************'+'\x1b[0m')
print("1. Action: You may play one action\n   card from your hand.\n   Follow the directions on the card")
print("2. Buy: You may purchase any one card\n   in a pile on the table. ")
print("3. Cleanup: The card you purchased,\n   all cards that you played,\n   cards remaining are placed\n   in your discard pile.")
print("4. Draw: Draw five cards from your deck\n   to replenish your hand. ")
print("5. Game ends when the last province is\n   bought or when three piles are empty.")
print('\x1b[3;34;47m'+'**************************************'+'\x1b[0m')


   
#Get player names
player_names = ["Annie","*Ben","*Carla"]

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
box["Council Room"]=[Dominion.Council_Room()]*10
box["Witch"]=[Dominion.Witch()]*10
box["Bureaucrat"]=[Dominion.Bureaucrat()]*10
box["Militia"]=[Dominion.Militia()]*10
box["Spy"]=[Dominion.Spy()]*10
box["Thief"]=[Dominion.Thief()]*10
box["Throne Room"]=[Dominion.Throne_Room()]*10

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

#Costruct the Player objects
players = []
for name in player_names:
    if name[0]=="*":
        players.append(Dominion.ComputerPlayer(name[1:]))
    elif name[0]=="^":
        players.append(Dominion.TablePlayer(name[1:]))
    else:
        players.append(Dominion.Player(name))

#Play the game
turn  = 0
while not Dominion.gameover(supply):

    turn += 1    
    print("\r")  
    print('\n\n')
    print('\x1b[3;34;47m'+'*****************************'+'\x1b[0m')
    print('\x1b[3;34;47m'+'**********  TABLE  **********'+'\x1b[0m')
    print("*****************************")
  
    for value in supply_order:
        print('\x1b[3;32;40m',"VALUE: ",value,'\x1b[0m')
        #print('\x1b[0m')
        for stack in supply_order[value]:
            
            if stack in supply:
                print ('\x1b[3;97;40m',stack, len(supply[stack]),'\x1b[0m')
                
        print("*****************************")
    print("\r")
    print('\x1b[3;34;47m'+'*****************************'+'\x1b[0m')
    print('\x1b[3;34;47m'+'**** PLAYERS AND SCORES *****'+'\x1b[0m')
    print('\x1b[3;34;47m'+'*****************************'+'\x1b[0m')


    for player in players:
        print (player.name,player.calcpoints())
    print("\n*****************************")
    print("Start of turn ", str(turn))
    print("*****************************")

    #print ("\r\nStart of turn " + str(turn))    
    for player in players:
        val = int(input("\nDo you want to see the action card abilities? [0]-YES [1]-NO   ")) 
        if val == 0:
            print_action_cards()
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
