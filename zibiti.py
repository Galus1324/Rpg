import sys, time, pygame, os
from pygame import mixer
from functions import *

drink=True
toa_map=True

# for typing sound
mixer.init()
mixer.music.load('sound.mp3')
mixer.music.set_volume(0.2)

def blacksmith():
    print_slow(go_to_blacksmith)
    circle_choice(["upgrade gear", "talk","leave"],
                 [lambda: print_slow(upgrade_1),
                  lambda: print_slow(blacksmith_talk_1)])
    print_slow(blacksmith_leave)
    
def merchant():
    print_slow(go_to_merchant)
    circle_choice(["buy", "what are you","tell me a story","leave"],
                  [lambda: (print_slow(merchant_buy),multi_choice(["potion","ring"],
                                                                   [lambda: print_slow(potion_of_healing),lambda: print_slow(ring_of_protection)])),
                   lambda: print_slow(what_am_i),
                   lambda: print_slow(tiefling_story)])
    print_slow(merchant_leave)

def wonder():
    print("wonder")
def journey_start():
    print_slow("journey")

# Example usage:
filename = "text_for_rpg.txt"
sections = load_sections("text_for_rpg.txt")

# Extract all sections automatically
extracted_sections = extract_sections(sections)

# Dynamically create variables from extracted sections
locals().update(extracted_sections)

print_slow(name)
player_name = input()
print_slow(intro)

multi_choice(["beer", "mead", "nothing"],
             [lambda: print_slow(beer),
              lambda: print_slow(mead),
              lambda: (print_slow(nothing),
                       globals().update({"drink": False}))])

print_slow(bartender_talk)

multi_choice(["yes", "no"],
             [lambda: print_slow(toa_yes),
              lambda: print_slow(toa_no)])

if drink:
    print_slow(drink_yes)
else:
    print_slow(drink_no)
    
print_slow(outside_village.format(player_name=player_name))

multi_choice(["yes", "no"],
             [lambda: print_slow(help_eirlys.format(player_name=player_name)),
              lambda: (print_slow(no_help_eirlys), globals().update({'toa_map': False})),])

if toa_map:
    print_slow("Do you wish to leave the village and go follow the map Towards the Tomb?\n")
    multi_choice(["yes", "no"],[lambda: journey_start(), lambda: None])

# If they stay in the village
print_slow(stay_in_the_village)
circle_choice(["blacksmith","merchaint","wonder", "go towards the tomb"],
              [lambda: blacksmith(), 
               lambda: merchant(), 
               lambda: wonder(), 
               lambda: journey_start()]) 





