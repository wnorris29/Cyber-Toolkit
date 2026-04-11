from utils.display import console
from rich.text import Text
from rich.panel import Panel
import pyfiglet
from utils.display import clear
from tools.hash_tools import hash_menu, hash_string, hash_file, compare_hashes
from tools.password_tools import password_menu, generate_password, rate_password
from tools.port_scanner import scan_menu, full_scan, custom_scan,popular_scan,run_custom_scan
from recon.whois_lookup import whois_menu,whois_lookup
import argparse


def print_banner():
    banner = pyfiglet.figlet_format("Cyber Toolkit", font='slant')
    text = Text(banner)
    text.stylize("bold cyan")
    text.stylize('magenta', 0, len(banner)//2)

    console.print(Panel(text))


def option_list():
    console.print("\nHere are your options:\n1: Password Tools\n2: Port scanner\n3: Hashing Tools\n4: WhoIS LookUp")

def take_input():
    option_list()
    pick = input('Please enter the number of the option you would like to pick, or enter 0 to quit \n')

    return pick

def validate_input():
    
    inpt = take_input()

    try:
        choice = int(inpt)

    except ValueError:
        return 'error'

    if choice == 1:
       
        return choice

    elif choice == 2:
    
        return choice

    elif choice == 3:
        return choice
    elif choice ==4:
        return choice

    elif choice == 0:
        return choice
    else:
        return 'invalid'
    
    

def script():

    print_banner()

    while True:
        
        choice = validate_input()
        clear()

        if choice == 0:
            console.print("Thanks for using me, Goodbye!")
            break
        elif choice == 1:
             console.print(f'You have chosen {choice}, the password tools\n')
        
             password_menu()

        elif choice == 2:
            console.print(f'You have chosen {choice}, the port scanner\n')
            
            scan_menu()

        elif choice == 3:
            console.print(f'You have chosen {choice}, the hashing tools\n')
            
            hash_menu()

        elif choice ==4:
            console.print(f'You have chosen {choice} WhoIsLookup ')
            whois_menu()

        

        elif choice == 'error':
            console.print('please enter a number\n')
        
            continue
        elif choice == 'invalid':
            console.print('Please enter a valid number')
            continue

        else:
            console.print('Please enter a valid number\n')

            continue


def parse_args():
    parser = argparse.ArgumentParser(description='Cyber Toolkit')

    parser.add_argument('--scan', choices = ['full', 'popular', 'custom'])
    parser.add_argument('--host', type=str)
    parser.add_argument('--port-range', nargs= 2, type=int)
    parser.add_argument('--hash', choices=['string', 'file','compare'])
    parser.add_argument('--pwd', choices=['generate', 'rate'])
    parser.add_argument('--whois',type= str )
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_args()
    if any(vars(args).values()):
        
        if args.scan:
            if not args.host:
                console.print('Host argument invalid')
                quit()
            elif args.scan == 'full':
                full_scan(args.host)
            elif args.scan =='popular':
                popular_scan(args.host)
            elif args.scan =='custom':
                if not args.port_range:
                    console.print('Port range argument invalid')
                    quit()
                else:
                    run_custom_scan(args.host,args.port_range[0],args.port_range[1])

        if args.hash:
            if args.hash =='string':
               result =  hash_string()
               console.print(result)
            elif args.hash =='file':
                result = hash_file()
                console.print(result)
            elif args.hash == 'compare':
                result = compare_hashes()
        if args.pwd:
            if args.pwd == 'generate':
                generate_password()
            elif args.pwd == 'rate':
                rate_password()
        if args.whois:
            whois_lookup(args.whois)
            





    else:
        script()



                 


