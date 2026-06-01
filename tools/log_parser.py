import re
from utils.display import console
from rich.table import Table


patterns = [
    (r'\.\./', 'Directory Traversal', 'High'),
    (r'SELECT|UNION|DROP|INSERT', 'SQL Injection', 'High'),
    (r'<script>', 'XSS Attempt', 'High'),
    (r'/admin|/wp-admin|/phpmyadmin','Admin Probing', 'Medium'),
    (r'sqlmap|nikto|nmap', 'Attack Tool Detected', 'High'),

]




def parse_log(filepath):
    findings = []

    try:
        with open(filepath, 'r') as f:
            for line_num, line in enumerate(f, 1):
                for pattern, name, risk in patterns:



                    if re.search(pattern, line, re.IGNORECASE):
                        ip = line.split()[0]
                        findings.append({
                            'line': line_num,
                            'ip': ip,
                            'pattern':name,
                            'risk': risk

                        })

            return findings 



    except FileNotFoundError:
        print('There was an error with the file, please try again')
        return
    




def display_findings(findings):


    
    if not findings:
        print('There are no findings to return!')
        return

    table = Table(title = 'Log Analysis Findings')

    table.add_column('line', style='cyan')
    table.add_column('IP', style='white')
    table.add_column('Pattern', style='magenta')
    table.add_column('Risk', style='white')


    for finding in findings:
        table.add_row(
            str(finding['line']),
            finding['ip'],
            finding['pattern'],
            finding['risk']
        )

    console.print(table)



def log_menu():

    while True:
        path = input('Please enter a filepath or type done to exit to main menu\n')

        if not path:
            print('please enter a value!')
            continue

        elif path == 'done':
            break
        else:
            findings = parse_log(path)
            display_findings(findings)
