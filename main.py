

import pyfiglet



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
       
        return 1 

    elif choice == 2:
    
        return 2

    elif choice == 3:
        return 3

    elif choice == 0:
        return 0
    else:
        print('You have not entered a valid number, please choose one of the options above, or enter 0 to quit.')
    

def script():

    print_banner()

    while True:
        choice = validate_input()

        if choice == 0:
            break
        elif choice == 1:
             print(f'You have chosen {choice}, the password tools')
             continue

        elif choice == 2:
            print(f'You have chosen {choice}, the port scanner')
            continue

        elif choice == 3:
            print(f'You have chosen {choice}, the hasing tools')
            continue

        

        elif choice == 'error':
            print('please enter a number')
            continue

        else:
            continue



if __name__ == '__main__':
    script()



                 


