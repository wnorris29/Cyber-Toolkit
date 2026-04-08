import socket 

def port_scanner_menu():
    print('Please choose a type of scan to conduct:\n1: Full Scan\n2: Popular Scan\n3: Custom Scan or type 0 to exit to main menu')



def take_input():

    port_scanner_menu()

    scan_type = input('Please choose one of the options\n')

    try:
        scan_type1 = int(scan_type)

    except:
        return 'error'
    
    if scan_type1 == 1:
        return 1
    elif scan_type1 ==2:
        return 2 
    elif scan_type1 == 3:
        return 3
    elif scan_type1 == 0:
        return 0
    else:
        return 'invalid'
    

def scan_menu():

    while True:

        choice = take_input()

        if choice == 1:
            print('You have chosen a full scan')
            host = get_host()
            full_scan(host)
        elif choice == 2:
            print('You have chosen a popular scan')
            host = get_host()
            popular_scan(host)
        elif choice == 3:
            print('You have chosen a custom scan')
            host = get_host()
            custom_scan(host)

        elif choice == 0:
            print('Exiting...')
            break
        elif choice == 'invalid':
            print('Please enter a valid number')
            continue
        elif choice == 'error':
            print('There was an error')
            continue



def scan_port(host, port):


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        is_open = sock.connect_ex((host, port))

        if is_open == 0:
            return True
        else:
            return False
        

def run_scan(host, ports):

    total = 0

    for port in ports:
        is_open = scan_port(host, port)

        if is_open == True:
            print(f'Port number {port} is open')
            total +=1

    print(f'There was {total} ports open')


def get_host():

    host = input('Enter the IP address you would like to scan\n')

    return host


def full_scan(host):
        
        ports = range(1,65536)
        run_scan(host, ports)


def popular_scan(host):

    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080]

    run_scan(host,ports)


def custom_scan(host):

    port1 = input('Enter the first port in the range')
    port2 = input('Enter the second port for the range')

    try:
        port_1 = int(port1)
        port_2 = int(port2)

    except:
        return 'error'
    
    

    
    if port_1 > port_2:
        print('The first number should be lower then the second number')
        return 'error'

    if port_1 <=0 or port_2 <=0:
        print('There is no port 0!')
        return 'error'

    

    
    if port_2 > 65535:
        print('Port is invalid!')
        return 'error'
    
    port_2 +=1
    
    
    ports = range(port_1, port_2)
    run_scan(host, ports)















    

        

