number_of_nazgul = 0
nazgul_on_battlefield = []
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def ask_for_input():
    clear_terminal()
    print(f"Nazgul on battlefield: {nazgul_on_battlefield}")
    user_input = int(input("(1) Add a nazgul to the battlefield\n"
                   "(2) Tempt the ring\n"
                   "(3) Remove a nazgul\n"
                   "(0) Exit"
                   "\nPlease enter what you would like to do:\n"
                   ))
    return user_input

def tempt_the_ring(nazgul):
    nazgul += number_of_nazgul



def add_nazgul():
    print(f"Nazgul already on the battlefield: {nazgul_on_battlefield}") 
    nazgul_to_add = input("Plesae enter the name of the Nazgul you'll be adding to the battlefield or type \"cancel\" to back out: ")
    if nazgul_to_add == 'cancel':
        print("\nbacking out")
    else:
        nazgul_on_battlefield.append(nazgul_to_add)
        
    print(f"\nnumber of Nazgul: {len(nazgul_on_battlefield)}\n")
    print(f"Nazgul on battlefield: {nazgul_on_battlefield}")

    
user_input = ask_for_input()

while user_input != 0:
    if user_input == 1:
        add_nazgul()
    user_input = ask_for_input()
