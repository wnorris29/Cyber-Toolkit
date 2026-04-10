import whois
from rich.table import Table
from utils.display import console


def whois_menu():

    print('Welcome to the WhoIS Lookup tool! Would you like to:\n0: Exit to main menu\n1: WhoIs Lookup')

    while True:
         
         choice = input('Please select an option\n')

         try:
              choice1 = int(choice)

         except ValueError:
              
              print('Enter a number')
              continue
         
         if choice1 == 0:
              print('Exiting...')
              break
         elif choice1 == 1:
              domain = get_domain()
              whois_lookup(domain)
              
         else:
              print('Enter a valid number')




    




def get_domain():



    domain = input('Enter a domain to lookup\n')

    return domain
    
def whois_lookup(domain):

    result = whois.whois(domain)

    table = Table(title="Whois Results")

    table.add_column("Field", style="green")
    table.add_column("Value", style="cyan")

    


    date = result.creation_date

    domain_name = result.domain_name

    exp_date = result.expiration_date

    if isinstance(exp_date, list):
         exp_date = exp_date[0]

    if isinstance(domain_name, list):
         
         domain_name = domain_name[0]

    if isinstance(date, list):
         date = date[0]


    table.add_row("Organisation", str(result.org) if result.org else "Unavailable")
    table.add_row("Domain name", str(domain_name) if result.domain_name else "Unavailable")
    table.add_row("Registrar", str(result.registrar) if result.registrar else "Unavailable")
    table.add_row("Creation date", str(date.strftime("%Y-%m-%d")) if result.creation_date else "Unavailable")
    table.add_row("Expiration Date", str(exp_date.strftime("%Y-%m-%d"))if result.expiration_date else "Unavailable")
    table.add_row("Country", str(result.country) if result.country else "Unavailable")
    table.add_row("Name Servers", ','.join(result.name_servers) if result.name_servers else "Unavailable")

    console.print(table)

