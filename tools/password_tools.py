import secrets
import string
def password_menu():
    
  

    while True:
        
        print('Would you like to: \n0: Return to menu \n1: Generate a password\n2: Rate a password.')

        chosen = handle_input()

        if chosen == 1:
            print('You have chosen to generate a password')
            generate_password()
        elif chosen == 2:
            print('You have chosen to rate a password')
            rate_password()
        elif chosen == 0:
            print('Returning to main menu...')
            break
        elif chosen == 'error':
            print("please enter a number")

        elif chosen == 'invalid':
            print('Please enter a valid number')

    


def handle_input():

    

    while True:
        chosen = input('Please choose a number from above\n')

        try:
            choice = int(chosen)

        except ValueError:
            return 'error'

        if choice == 1:
            return 1
        elif choice == 2:
            return 2
        elif choice == 0:
            return 0
        else:
            return 'invalid'
        


def generate_password():

    pwd = ''

    length = input('How long would you like the password to be?\n')

    try:
        length1 = int(length)

    except ValueError:
        print('please enter a number')
        return 'error'
    
    char_pool = []
    
    while True:
        char_pool_to_add = input('Please select some of the following:\n1: Lowercase\n2: Uppercase\n3: Numbers\n4: Special Characters then type done when you are ready!')

        if char_pool_to_add == 'done':
            break
        
        try:
            char_pool_to_add1 = int(char_pool_to_add)

        except ValueError:
            print('Please enter a a number')
            return 'error'
        
        if char_pool_to_add1 == 1:
            char_pool += string.ascii_lowercase
            
        elif char_pool_to_add1 == 2:
            char_pool += string.ascii_uppercase
            

        elif char_pool_to_add1 == 3:
            char_pool += string.digits
            

        elif char_pool_to_add1 ==4:
            char_pool += string.punctuation

        else:
            print('Enter a valid number')
            

    
    if len(char_pool) == 0:
        print('You have not selected anything! Please try again')
        return 'empty'
    
    for pools in range(length1):
        pwd += secrets.choice(char_pool)

    print(pwd)
    return pwd




def rate_password():

    pwd = input('Enter the password you would like to rate.\n')
    score = 0

    if len(pwd) >8:
        score +=1

    if any(c in string.ascii_lowercase for c in pwd):
        score+=1

    if any(c in string.ascii_uppercase for c in pwd):
        score +=1

    if any(c in string.digits for c in pwd):
        score+=1

    if any(c in string.punctuation for c in pwd):
        score+=1

    if score == 1 or score == 2:
        print('Your password is weak')

    elif score == 3 or score == 4:
        print('Your password is moderate')

    elif score == 5:
        print('Your password is strong')

    elif score ==0 :
        print('Your password is very weak!!')

    

    

        

    

        

        



        



