import os
number_of_nazgul = 0
nazgul_on_battlefield = []


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def ask_for_input():
    clear_terminal()
    display_nazgul()
    user_input = int(input("(1) Add a nazgul to the battlefield\n"
                   "(2) Tempt the ring\n"
                   "(3) Remove a nazgul\n"
                   "(0) Exit"
                   "\n\nPlease enter what you would like to do: "
                   ))
    return user_input

def tempt_the_ring():
    
    roaming_throne_on_battlefield = False
    
    for name in nazgul_on_battlefield:
        if name["name"] == 'roaming throne':
            roaming_throne_on_battlefield = True

    for counter in nazgul_on_battlefield:
        if not roaming_throne_on_battlefield:
            counter["counters"] += int(len(nazgul_on_battlefield))
        elif roaming_throne_on_battlefield:
            counter["counters"] += int((len(nazgul_on_battlefield) - 1) * 2)
 

def display_nazgul():
    names = []
    counters = 0
    
    if len(nazgul_on_battlefield) == 0:
        print("\nNo Nazgul on battlefield yet\n")
        return
    for name in nazgul_on_battlefield:
        names.append(name["name"])
    print("Nazgul on the battlefield: ", end='')
    for nazgul in names:
        print(nazgul, end=', ')
    print("\n\n")
    for display in nazgul_on_battlefield:
        print(f"Counters on Nazgul: {display["name"]} has {display["counters"]} counters.\n")

def add_nazgul():
    clear_terminal()
    display_nazgul() 
    nazgul_name = ''
    counters = 0
    

    while True:
        nazgul_name = input("Plesae enter the name of the Nazgul you'll be adding to the battlefield or type \"cancel\" to back out: ")
        
        if nazgul_name == 'cancel':
            return
        
        nazgul_already_in_play = False

        for nazgul in nazgul_on_battlefield:
            if nazgul["name"] == nazgul_name:
                nazgul_already_in_play = True
                
        if nazgul_already_in_play:
            print("Please enter a name not already on the list")
        else:
            break

    nazgul_to_add = {
        "name": nazgul_name,
        "counters": counters
    }

    nazgul_on_battlefield.append(nazgul_to_add)

    print(f"\nnumber of Nazgul: {len(nazgul_on_battlefield)}\n")
    
        
user_input = ask_for_input()

while user_input != 0:
    if user_input == 1:
        add_nazgul()
    if user_input == 2:
        tempt_the_ring()
    user_input = ask_for_input()

