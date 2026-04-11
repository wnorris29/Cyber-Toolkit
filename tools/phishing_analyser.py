from tools.virustotal import scan_url
from recon.whois_lookup import whois_lookup
from utils.display import console
from urllib.parse import urlparse
import re
import requests
from datetime import datetime, timezone, timedelta
import whois
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv('VT_API_KEY')

def phishing_menu():
    while True:
        console.print('Please enter a URL to test or enter done to return to menu\n')

        url = input('enter a URL\n')

        if url == 'done':
            console.print('Exiting...')
            break

        else:
            domain = urlparse(url).netloc
            heuristic_warnings = heuristic_check(url)
            domain_warnings = domain_age_check(domain)
            redirect_warnings = redirect_check(url)
            vt_result = scan_url(url, api_key)

            risk, score, colour = calculate_risk(vt_result, heuristic_warnings, domain_warnings, redirect_warnings)
            all_warnings = heuristic_warnings + domain_warnings + redirect_warnings

            if all_warnings:
                for warning in all_warnings:
                    console.print(f'! {warning}', style='bold yellow')

            else:
                console.print('No warnings found', style = 'bold green')
            console.print(f'\nRisk Level: {risk} (Score: {score})', style = f'bold {colour}')

                








def heuristic_check(url):
    warnings = []
    parsed = urlparse(url)
    suspicious_tlds = ['.xyz', '.top', '.tk', '.ml', '.ga', '.cf']

    if len(url) > 75:
        warnings.append("URL is excessively long")

    if parsed.scheme != 'https':
        warnings.append("URL does not use HTTPS")


    if re.match(r'\d+\.\d+\.\d+\.\d+', parsed.netloc):
        warnings.append("URL uses an IP address instead of a domain name")

    if len(parsed.netloc.split('.')) > 4:
        warnings.append('URL has excessive subdomains')

    if '@' in url:
        warnings.append('URL contains @ symobl - real destination may be hidden')

    if parsed.netloc.count('-') > 3:
        warnings.append('Domain contains excessive hyphens')

    if any(parsed.netloc.endswith(tld) for tld in suspicious_tlds):
        warnings.append('URL uses a suspicious TLD')

    
    return warnings


def domain_age_check(domain):

    warnings = []

    try:
        six_months_ago = datetime.now(timezone.utc) - timedelta(days=180)
        results = whois.whois(domain)
        date = results.creation_date



        if isinstance(date,list):
            date = date[0]

        if date.tzinfo is None:
            date = date.replace(tzinfo=timezone.utc)

        if date > six_months_ago:
            warnings.append('Domain was created less than 6 months ago')

    except Exception:
        warnings.append('Could not determine domain age')
    return warnings


def redirect_check(url):
    warnings = []

    try:
        response = requests.get(url, allow_redirects=True, timeout=5)

        final_url = response.url

        if final_url != url:
            warnings.append('The URL contains some redirects')
    except requests.exceptions.RequestException:
        warnings.append('Could not follow the URL')
    return warnings


def calculate_risk(vt_results, heuristic_warnings, domain_warnings, redirect_warnings):
    
    score = 0
    
    if vt_results >0:
        score+=3

    score+=len(domain_warnings)
    score+= len(heuristic_warnings)
    score += len(redirect_warnings)

    if score ==0:
        risk = 'low'
        colour = 'green'
    elif score <=2:
        risk = 'suspicious'
        colour = 'yellow'
    else:
        risk = 'high risk'
        colour = 'red'

    return risk,score,colour
