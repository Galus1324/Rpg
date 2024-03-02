import sys, time, pygame, os
from pygame import mixer

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
       
        variable_name = heading.replace(" ", "_").lower()
        extracted_variables[variable_name] = content
    
    return extracted_variables

def play_sound(sound, channel):
    channel.play(sound)

# Function for printing text slowly
def print_slow(args):
    play_sound(sound1, channel1)
    for arg in args:
        for char in arg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.001)
    channel1.stop()

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