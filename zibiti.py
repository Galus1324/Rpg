import sys, time, os, random
from pygame import mixer
from functions import *
from combat_stuff import *
from music import *



drink=True
toa_map=True

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

def choose_potion():
    print_slow(potion_of_healing)
    player.health_potion = True

def choose_ring():
    print_slow(ring_of_protection)
    player.armor_class += 1
    player.armor_class_base += 1

def merchant():
    print_slow(go_to_merchant)
    circle_choice(["buy", "what are you","tell me a story","leave"],
                  [lambda: (print_slow(merchant_buy),multi_choice(["potion","ring"],
                                                                   [lambda: choose_potion(),
                                                                    lambda: choose_ring()])),
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
    print_slow(escaping_forest)
    player.rest()

def fighting_goblins():
    print_slow(goblin_battle)
    combat(player, goblin_1)
    combat(player, goblin_2)
    if toa_map:
        print_slow(goblin_win)

def room_2():
    print("room_2")

def room_3():
    print("room_3")

def book():
    print_slow(read_book)   

def lockpick_left():
    print_slow(lockpick_door)
    if player.lockpicking():
        print_slow(open_door)
        room_2()
    else:
        print_slow(not_open_door)
        book()

def lockpick_right():
    print_slow(lockpick_door)
    if player.lockpicking():
        print_slow(open_door)
        room_3()
    else:
        print_slow(not_open_door)
        book()
    
def dungeon():
    print_slow(dungeon_room1)
    multi_choice(["lockpick left door","lockpick right door", "go to the book"],
                 [lambda: lockpick_left(),
                  lambda: lockpick_right(),
                  lambda: book()])


def journey_start():
    play_sound(jungle_music, channel2)
    print_slow(journey)
    if not toa_map:
        get_lost()
    else:
        pass
    print_slow(goblins)
    multi_choice(["fight", "run away"],
                 [lambda: fighting_goblins(),
                  lambda: print_slow(goblin_run) ])
    print_slow(peaceful_travel)
    player.rest()
    dungeon()



filename = "text_for_rpg.txt"
sections = load_sections("text_for_rpg.txt")

# Extract all sections automatically
extracted_sections = extract_sections(sections)

# Dynamically create variables from extracted sections
locals().update(extracted_sections)

try:
    print_slow(class_selection)

    multi_choice(["fighter", "mage", "rogue"],
                [select_fighter,
                select_mage,
                select_rogue])

    print_slow(name)

    player.name = input()

    play_sound(village_music, channel2)
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
        multi_choice(["yes", "no"],
                    [lambda: journey_start(),
                    lambda: None])

    # If they stay in the village
    print_slow(stay_in_the_village)
    circle_choice(["blacksmith","merchant","wonder", "go towards the tomb"],
                [lambda: blacksmith(), 
                lambda: merchant(), 
                lambda: wonder(),
                lambda: journey_start()])


except GameOverException as e:
    pass






