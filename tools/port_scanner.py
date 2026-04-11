import socket 
from utils.display import console
from rich.table import Table




services = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    445: 'SMB',
    3306: 'MySQL',
    3389: 'RDP',
    8080: 'HTTP Alternate'
}



def port_scanner_menu():
    console.print('Please choose a type of scan to conduct:\n1: Full Scan\n2: Popular Scan\n3: Custom Scan or type 0 to exit to main menu')



def take_input():

    port_scanner_menu()

    scan_type = input('Please choose one of the options\n')

    try:
        scan_type1 = int(scan_type)

    except ValueError:
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
            console.print('You have chosen a full scan')
            host = get_host()
            full_scan(host)
        elif choice == 2:
            console.print('You have chosen a popular scan')
            host = get_host()
            popular_scan(host)
        elif choice == 3:
            console.print('You have chosen a custom scan')
            host = get_host()
            custom_scan(host)

        elif choice == 0:
            console.print('Exiting...')
            break
        elif choice == 'invalid':
            console.print('Please enter a valid number')
            continue
        elif choice == 'error':
            console.print('There was an error')
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

    console.print("Scan started...", style = 'bold green')

    total = 0

    table = Table(title= "Scan Results")

    table.add_column("Port", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Service", style="magenta")


    for port in ports:
        is_open = scan_port(host, port)

        if is_open == True:
            total +=1

            table.add_row(str(port), "open", services.get(port, "Unknown") )

    console.print(table)

    if total > 0:

        console.print(f'There was {total} ports open', style='bold green')
    else:
        console.print('No open ports found', style='bold red')


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

    except ValueError:
        return 'error'
    
    

    

    
    

    run_custom_scan(host, port_1, port_2)




def run_custom_scan(host, port1,port2):
      
    if port1 > port2:
        console.print('The first number should be lower then the second number')
        return 'error'

    if port1 <=0 or port2 <=0:
        console.print('There is no port 0!')
        return 'error'

    

    
    if port2 > 65535:
        console.print('Port is invalid!')
        return 'error'
    
    port2 +=1
    
    
    ports = range(port1, port2)
    run_scan(host, ports)

    
















    

        

