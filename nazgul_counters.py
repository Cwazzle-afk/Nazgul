number_of_nazgul = 1
nazgul_on_battlefield = []

def ask_for_input():
    user_input = int(input("(1) Add a nazgul to the battlefield\n"
                   "(2) Tempt the ring\n"
                   "(3) Remove a nazgul\n"
                   "(0) Exit"
                   "\nPlease enter what you would like to do:\n"
                   ))
    return user_input

def calculate_counters_on_nazgul(nazgul):
    nazgul += number_of_nazgul

def add_nazgul():
    print(f"Nazgul already on the battlefield: {nazgul_on_battlefield}") 
    nazgul_to_add = input("Plesae enter the name of the Nazgul you'll be adding to the battlefield or type cancel to back out: ")
    if nazgul_to_add == 'cancel':
        print("\nbacking out")
    #elif add da shit to da list
    print(f"\nnumber of Nazgul: {number_of_nazgul}\n")

user_input = ask_for_input()

while user_input != 0:
    if user_input == 1:
        add_nazgul()
    user_input = ask_for_input()



