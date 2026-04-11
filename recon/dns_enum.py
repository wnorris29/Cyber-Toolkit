from utils.helpers import get_domain
from utils.display import console
import dns.resolver
from rich.table import Table

def dns_menu():

    


    while True:


        console.print('Please select one of the following:\n0: Return to main menu\n1: Query all record types\n2: A record\n3: AAAA record \n4: MX record\n5: NS record\n6: TXT record\n7:CNAME record ')


        choice = input('Please enter a number from above:\n')

        try:
            choice = int(choice)

        except ValueError:
            console.print('Please enter a number', style='bold red')
            continue

        if choice == 0:
            console.print('Exiting to main menu...')
            break
        elif choice == 1:
            console.print(f'You have selcted {choice}, all record types')
            domain = get_domain()
            dns_lookup(domain, 'A')
            dns_lookup(domain, 'AAAA')
            dns_lookup(domain, 'MX')
            dns_lookup(domain, 'NS')
            dns_lookup(domain, 'TXT')
            dns_lookup(domain, 'CNAME')
        elif choice == 2:
            console.print(f'You have chosen {choice}, A record')
            domain = get_domain()
            dns_lookup(domain, 'A')
        elif choice == 3:
            console.print(f'You have chosen {choice}, AAAA record')
            domain = get_domain()
            dns_lookup(domain, 'AAAA')
        elif choice ==4:
            console.print(f'You have chosen {choice}, MX record')
            domain = get_domain()
            dns_lookup(domain, 'MX')
        elif choice ==5:
            console.print(f'You have chosen {choice}, NS record')
            domain = get_domain()
            dns_lookup(domain, 'NS')
           
        elif choice == 6:
            console.print(f'You have chosen {choice}, TXT record')
            domain = get_domain()
            dns_lookup(domain, 'TXT')
           
        elif choice == 7:
            console.print(f'You have chosen {choice}, CNAME record')
            domain = get_domain()
            dns_lookup(domain, 'CNAME')
           

        else:
            console.print('Please enter a valid number', style='bold red')



def dns_lookup(domain, record_type):

    table = Table(title='DNS Results')

    table.add_column('Record Type', style='cyan')
    table.add_column('Value', style='magenta')


    try:
        results = dns.resolver.resolve(domain, record_type)
        for result in results:
            table.add_row(record_type, result.to_text())
        console.print(table)

    except dns.resolver.NoAnswer:
        console.print(f'No {record_type} records found', style='bold red')

    except dns.resolver.NXDOMAIN:
        console.print('Domain does not exist', style='bold red')

    
                      












