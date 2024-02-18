import sys, time, pygame, os
from pygame import mixer

drink=True
toa_map=True

# for typing sound
mixer.init()
mixer.music.load('sound.mp3')
mixer.music.set_volume(0.2)

# Function to load sections from the text file
def load_sections(filename):
    with open(filename, "r") as file:
        text = file.read()

    sections = {}
    current_section = {"heading": None, "content": ""}

    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("===") and line.endswith("==="):
            if current_section["heading"] is not None:
                sections[current_section["heading"]] = current_section["content"]
            current_section = {"heading": line[4:-4].strip(), "content": ""}
        else:
            current_section["content"] += line + "\n"

    if current_section["heading"] is not None:
        sections[current_section["heading"]] = current_section["content"]

    return sections

# Function to extract sections and create variables dynamically
def extract_sections(sections):
    extracted_variables = {}
    
    for heading, content in sections.items():
        # Convert heading to a valid variable name (replace spaces with underscores and make it lowercase)
        variable_name = heading.replace(" ", "_").lower()
        extracted_variables[variable_name] = content
    
    return extracted_variables

# Function for printing text slowly
def print_slow(args):
    mixer.music.play()
    for arg in args:
        for char in arg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.001)
    mixer.music.stop()

# Function for multiple choice interactions
def multi_choice(answers, consequences):
    print_slow("Choose an option:\n")
    print_slow(f"Available answers: {', '.join(answers)}\n")
    x = input().lower()

    if x not in answers:
        print_slow(f"Your answer '{x}' is not valid.\n")
        multi_choice(answers, consequences)
    else:
        index = answers.index(x)
        consequences[index]()

# for looping choices
def circle_choice(answers, consequences):
    while answers:
        print_slow("Choose an option:\n")
        print_slow(f"Available answers: {', '.join(answers)}\n")
        x = input().lower()

        if x == "leave":
            print_slow("You chose to leave.\n")
            break
        elif x not in answers:
            print_slow(f"Invalid answer '{x}'\n")
        else:
            index = answers.index(x)
            consequences[index]()
            del answers[index]
            del consequences[index]

def blacksmith():
    print_slow(go_to_blacksmith)
    circle_choice(["upgrade gear", "talk","leave"],
                 [lambda: print_slow(upgrade_1),
                  lambda: print_slow(blacksmith_talk_1)])
    print_slow(blacksmith_leave)
    
def merchaint():
    print_slow(go_to_merchaint)
    circle_choice(["buy", "what are you","tell me a story","leave"],
                  [lambda: (print_slow(merchaint_buy),multi_choice(["potion","ring"],
                                                                   [lambda: print_slow(ring_of_protection),lambda: print_slow(potion_of_healing)])),
                   lambda: print_slow(what_am_i),
                   lambda: print_slow(tiefling_story)])
    print_slow(merchaint_leave)


def tavern_2():
    print("tavern")
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
circle_choice(["blacksmith","merchaint","tavern","wonder", "go towards the tomb"],
              [lambda: blacksmith(), 
               lambda: merchaint(), 
               lambda: tavern_2(), 
               lambda: wonder(), 
               lambda: journey_start()]) 





