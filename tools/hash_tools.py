import hashlib
from utils.display import console

def hash_option_list():
    console.print('Please pick one of the following:\n0: Return to main menu\n1: Hash a string\n2: Hash a file\n3: compare two hashes.')

def take_input():
    hash_option_list()
    choice = input('Please choose an option\n')

    return choice


def handle_input():

    inpt = take_input()

    try:
        choice = int(inpt)

    except ValueError:
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
            console.print('You have chosen to hash a string')
            console.print(hash_string())
        elif choice == 2:
            console.print('You have chosen to hash a file')
            console.print(hash_file())

        elif choice == 3:
            console.print('You have chosen to compare two hashes')
            compare_hashes()

        elif choice == 0:
            console.print('Exiting to main menu...')
            break

        elif choice == 'invalid':
            console.print('Please enter a valid number')
            continue


def pick_algorithm():

    console.print('Here are your algorithm choices:\n1: md5\n2: sha1\n3:sha256\n')

    

    while True:
        alg_choice = input('please enter a number\n')
        try:
            choice = int(alg_choice)

        except ValueError:
            console.print('Please enter a number')
            continue

        if choice == 1:
            console.print('You have picked md5')
            return 'md5'
        elif choice == 2:
            console.print('You have picked sha1')
            return 'sha1'
        elif choice == 3:
            console.print('You have picked sha256')
            return 'sha256'
        else:
            console.print('Enter a valid number')
            continue


    


def hash_string():

    pre_string = input('Please enter a string you would like to hash\n')

    alg = pick_algorithm()

    if alg == 'md5':
        post_string = hashlib.md5(pre_string.encode()).hexdigest()
        

    elif alg == 'sha1':
        post_string = hashlib.sha1(pre_string.encode()).hexdigest()
        

    elif alg == 'sha256':
        post_string = hashlib.sha256(pre_string.encode()).hexdigest()
    
    

    return post_string


def hash_file():

    pre_file = input('enter a filename to be hashed\n')

    alg = pick_algorithm()

    try:
        with open(pre_file, 'rb') as f:
            contents = f.read()
            if alg == 'md5':
                post_file = hashlib.md5(contents).hexdigest()

            elif alg =='sha1':
                post_file = hashlib.sha1(contents).hexdigest()

            elif alg == 'sha256':
                post_file = hashlib.sha256(contents).hexdigest()

            
            return post_file


    except FileNotFoundError:
        console.print('There was an error')


def compare_hashes():

    file_or_string = input('Would you like to  compare string hashes or  compare file hashes (file/string)\n')

   

    if file_or_string == 'file':
        unknown_hash = hash_file()
       
        

    elif file_or_string == 'string' :
       unknown_hash = hash_string()

    else:
        console.print('Enter a valid choice')
        return 'error'
    

    known_hash = input('Enter the known hash\n')
       
      

    if unknown_hash == known_hash:
            console.print('They match')

    else:
            console.print('They do not')



    
    
    

    

