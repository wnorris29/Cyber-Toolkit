import whois


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


    date = result.creation_date

    domain_name = result.domain_name

    exp_date = result.expiration_date

    if isinstance(exp_date, list):
         exp_date = exp_date[0]

    if isinstance(domain_name, list):
         
         domain_name = domain_name[0]

    if isinstance(date, list):
         date = date[0]


    if result.org:
         print(f'Organisation: {result.org}')
    else:
         print('Organisation: Not available')

    if result.domain_name:
         print(f'Domain Name: {domain_name}')

    else:
         print('Domain Name: Unavailable')

    if result.registrar:
         print(f'Registrar: {result.registrar}')

    else:
         print('Registrar: Unavailable')

    if result.creation_date:
         print(f'Creation Date: {date.strftime("%Y-%m-%d")}')

    else:
         print('Creation Date: Unavailable')

    if result.expiration_date:
         print(f'Expiration Date: {exp_date.strftime("%Y-%m-%d")}')

    else:
         print('Expiration Date: Unavailable')

    if result.country:
         print(f'Country: {result.country}')

    else:
         print('Country: Unavailable')

    if result.name_servers:
         print(f'Name Servers: {", ".join(result.name_servers)}')

    else:
         print('Name Servers: Unavailable')


