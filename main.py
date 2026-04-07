

import pyfiglet
from utils.display import clear
from tools.hash_tools import hash_menu
from tools.password_tools import password_menu




def print_banner():
    banner = pyfiglet.figlet_format("Cyber Toolkit")

    print(banner)


def option_list():
    print("\nHere are your options:\n1: Password Tools\n2: Port scanner\n3: Hashing Tools")

def take_input():
    option_list()
    pick = input('Please enter the number of the option you would like to pick, or enter 0 to quit \n')

    return pick

def validate_input():
    
    inpt = take_input()

    try:
        choice = int(inpt)

    except:
        return 'error'

    if choice == 1:
       
        return choice

    elif choice == 2:
    
        return choice

    elif choice == 3:
        return choice

    elif choice == 0:
        return choice
    
    

def script():

    print_banner()

    while True:
        
        choice = validate_input()
        clear()

        if choice == 0:
            print("Thanks for using me, Goodbye!")
            break
        elif choice == 1:
             print(f'You have chosen {choice}, the password tools\n')
        
             password_menu()

        elif choice == 2:
            print(f'You have chosen {choice}, the port scanner\n')
            
            continue

        elif choice == 3:
            print(f'You have chosen {choice}, the hashing tools\n')
            
            hash_menu()

        

        elif choice == 'error':
            print('please enter a number\n')
        
            continue

        else:
            print('Please enter a valid number\n')

            continue



if __name__ == '__main__':
    script()



                 


