import sys, time, pygame, os, random
from pygame import mixer
from functions import *
from combat_stuff import *



drink=True
toa_map=True


# for typing sound
mixer.init()
mixer.music.load('sound.mp3')
mixer.music.set_volume(0.2)

def select_fighter():
    global player
    player = fighter
    print_slow("You selected Fighter.\n")

def select_mage():
    global player
    player = mage
    print_slow("You selected Mage.\n")

def select_rogue():
    global player
    player = rogue
    print_slow("You selected Rogue.\n")

def upgrade_armor():
    print_slow(upgrade_1)
    player.armor_class += 1
    player.armor_class_base += 1

def blacksmith():
    print_slow(go_to_blacksmith)
    circle_choice(["upgrade gear", "talk","leave"],
                 [lambda: upgrade_armor(),
                  lambda: print_slow(blacksmith_talk_1)])
    print_slow(blacksmith_leave)
    
def merchant():
    print_slow(go_to_merchant)
    circle_choice(["buy", "what are you","tell me a story","leave"],
                  [lambda: (print_slow(merchant_buy),multi_choice(["potion","ring"],
                                                                   [lambda: print_slow(potion_of_healing),
                                                                    lambda: print_slow(ring_of_protection)])),
                   lambda: print_slow(what_am_i),
                   lambda: print_slow(tiefling_story)])
    print_slow(merchant_leave)

def wonder():
    print_slow(wonder_shack)
    multi_choice(["go inside","ignore"],
                 [lambda: enen_talk(),
                  lambda: print_slow(ignore),])

def enen_talk():
    print_slow(enen_the_wise)
    circle_choice(["village history","tomb history","enen past","leave"],
                  [lambda: print_slow(village_history),
                   lambda: print_slow(tomb_history),
                   lambda: print_slow(enen_past)])
    print_slow(enen_leave)

def get_lost():
    print_slow(getting_lost)
    combat(player, triceratops)

def journey_start():
    print_slow(journey)
    if not toa_map:
        get_lost()
    else:
        pass

filename = "text_for_rpg.txt"
sections = load_sections("text_for_rpg.txt")

# Extract all sections automatically
extracted_sections = extract_sections(sections)

# Dynamically create variables from extracted sections
locals().update(extracted_sections)

print_slow(class_selection)

multi_choice(["fighter", "mage", "rogue"],
             [select_fighter,
              select_mage,
              select_rogue])

print_slow(name)

player.name = input()

get_lost()

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
circle_choice(["blacksmith","merchant","wonder", "go towards the tomb"],
              [lambda: blacksmith(), 
               lambda: merchant(), 
               lambda: wonder(), 
               lambda: journey_start()])
 





