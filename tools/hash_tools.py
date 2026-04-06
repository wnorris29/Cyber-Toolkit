

def hash_option_list():
    print('Please pick one of the following:\n0: Return to main menu\n1: Hash a string\n2: Hash a file\n3: compare two hashes.')

def take_input():
    hash_option_list()
    choice = input('Please choose an option\n')

    return choice


def handle_input():

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
        return 'invalid'
    

def hash_menu():

    while True:
        choice = handle_input()

        if choice == 1:
            print('You have chosen to hash a string')
            continue
        elif choice == 2:
            print('You have chosen to hash a file')
            continue

        elif choice == 3:
            print('You have chosen to compare two hashes')
            continue

        elif choice == 0:
            print('Exiting to main menu...')
            break

        elif choice == 'invalid':
            print('Please enter a valid number')
            continue

    


