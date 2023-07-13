# This is my attempt to recreate the game Zombiedice from Steve Jackson Games in python.
# it is pretty fun a push-your-luck game of dice

import random
import time
from collections import Counter

green_die = ['shot' for _ in range(1)] + ['walk' for _ in range(2)] + ['brain' for _ in range(3)]
yellow_die = ['shot' for _ in range(2)] + ['walk' for _ in range(2)] + ['brain' for _ in range(2)]
red_die = ['shot' for _ in range(3)] + ['walk' for _ in range(2)] + ['brain' for _ in range(1)]

dice = ['red' for _ in range(3) ] + ['yellow' for _ in range(4)] + ['green' for _ in range(6)]

while True:
    number_of_players = input('How many players will be playing? (1 to 6)')
    if number_of_players.isdigit():
        number_of_players = int(number_of_players)
        if 1 <= number_of_players <= 6:
            break
        else:
            print('Must be a number between 1 and 6, try again.')
    else:
        print('Must be a number between 1 and 6, try again.')
    

players_score = [0 for _ in range(number_of_players)]

available_dice = dice.copy()

def draft(dice_number, available_dice):
    drafted_dice = []
    max_loop = min(dice_number, len(available_dice))
    for _ in range(max_loop):
        random.shuffle(available_dice)
        color = available_dice.pop(0)
        # color = available_dice.pop(random.randint(0, len(available_dice)-1))
        drafted_dice.append(color)
    return drafted_dice
        

def roll(curr_dice):
    curr_roll = []
    for color in curr_dice:
        die = []
        if color == 'red':
            die = {'color': 'red', 'face': red_die[random.randint(0, 5)]}
        elif color == 'yellow':
            die = {'color': 'yellow', 'face': yellow_die[random.randint(0, 5)]}
        elif color == 'green':
            die = {'color': 'green', 'face': green_die[random.randint(0, 5)]}
        curr_roll.append(die)
    return curr_roll


player = 1

while max(players_score) < 13:
    available_dice = dice.copy()
    print(f"Player {player}'s turn:")
    time.sleep(1)
    shots = 0
    walks = 0
    brains = 0
    final_roll = []
    curr_dice = draft(3, available_dice)
    curr_roll = roll(curr_dice)
    
    print(f"Player {player} rolled: ")
    for die in curr_roll:
        print("  "+ f"{die['color']}: {die['face']}")

    for idx in range(len(curr_roll)):
        die = curr_roll[idx]
        color, face = die['color'], die['face']
        if face == 'shot':
            shots += 1
            curr_dice.remove(color)
            final_roll.append(die)
        elif face == 'walk':
            walks += 1
        elif face == 'brain':
            brains += 1
            curr_dice.remove(color)
            final_roll.append(die)


    print(f"Player {player}'s current round's results are: ")
    for die in final_roll:
        print("  "+ f"{die['color']}: {die['face']}")

    while shots < 3:
        curr_dice_count = dict(Counter(curr_dice))
        av_dice_count = dict(Counter(available_dice))
        if len(available_dice) < 1:
            break
        print(f"current_dice: {curr_dice_count}")
        reroll = input(f"available_dice: {av_dice_count} \n Do you want to keep rolling? (y/n) \n ")
        if reroll.upper() == "Y":
            curr_dice += draft((3 - walks), available_dice)
            curr_roll = roll(curr_dice)
            
            print(f"Player {player} rolled: ")
            print(curr_roll)
            for die in curr_roll:
                print("  "+ f"{die['color']}: {die['face']}")
            walks = 0
            for idx in range(len(curr_roll)):
                die = curr_roll[idx]
                color, face = die['color'], die['face']
                if face == 'shot':
                    shots += 1
                    curr_dice.remove(color)
                    final_roll.append(die)
                elif face == 'walk':
                    walks += 1
                elif face == 'brain':
                    brains += 1
                    curr_dice.remove(color)
                    final_roll.append(die)
        elif reroll.upper() == "N":
            break
        else:
            print('Invalid answer, try again. (y/n)')
        print(f"Player {player}'s current round's results are now: ")
        for die in final_roll:
            print("  "+ f"{die['color']}: {die['face']}")


    if shots >= 3:
            print(f"Player {player} got shot three times! No score this turn.")
            time.sleep(2)
    else:
        players_score[player - 1] += brains
        print(f"Player {player} devoured {brains} brains this round. \nPlayer {player}'s score is at: {players_score[player - 1]}")
        time.sleep(2)

    print('Current players scores:')
    for idx, score in enumerate(players_score):
        print(f'Player {idx + 1}: {score} points! ')
    input('Press enter for next round.')

    player += 1
    if player > number_of_players:
        player = 1

1
winner_score = max(players_score)
winner = players_score.index(winner_score)
print(f"Player {winner + 1} wins!")
    

    

        


        
