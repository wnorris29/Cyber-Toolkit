from utils.display import console
import requests
from rich.table import Table
from dotenv import load_dotenv
import os
import time

load_dotenv()
api_key = os.getenv('VT_API_KEY')

def vt_menu():

    while True:

        url = input('Please enter a URL or type done to exit\n')

        if not url:
            console.print('Please enter a URL', style='bold red')

        elif url == 'done':
            console.print('exiting to menu...')
            break
        else:
            scan_url(url, api_key)


def scan_url(url, api_key):



    try:
        headers = {'x-apikey': api_key}
        response = requests.post(
            'https://www.virustotal.com/api/v3/urls',
            headers = headers,
            data  = {'url' : url}
        )

        if response.status_code != 200:
            console.print(f'Error: {response.json()["error"]["message"]}', style='bold red')
            return



        analysis_id = response.json()['data']['id']

        console.print('Analysisng...', style='bold yellow')
        while True:
            result = requests.get(f'https://www.virustotal.com/api/v3/analyses/{analysis_id}',headers = headers)
            status = result.json()['data']['attributes']['status']
            if status == 'completed':
                break
            time.sleep(2)

      

      

        stats = result.json()['data']['attributes']['stats']
        malicious = stats['malicious']
        suspicious = stats['suspicious']
        harmless = stats['harmless']
        undetected = stats['undetected']


        table = Table(title=f'VirusTotal Results: {url}')
        table.add_column('Category', style='white')
        table.add_column('Count', style='white')

        table.add_row('Malicious', str(malicious), style='bold red')
        table.add_row('Suspicious', str(suspicious), style='yellow')
        table.add_row('Harmless', str(harmless), style='green')
        table.add_row('Undetected', str(undetected))

        console.print(table)

    except requests.exceptions.RequestException:
        console.print('Network Error - check your connection', style='bold red')


