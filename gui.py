import customtkinter as tk
import hashlib
import threading
from tools.port_scanner import scan_port
import whois
import dns.resolver
from dotenv import load_dotenv
import os
import requests
import time
from tools.phishing_analyser import heuristic_check, domain_age_check, redirect_check, calculate_risk
from urllib.parse import urlparse
from tools.virustotal import scan_url

load_dotenv()
api_key = os.getenv('VT_API_KEY')


def show_frame(frame):
    frame.tkraise()






def run_hash():
    
    algorithm = hashing_options.get().lower()
    mode = hash_mode.get()

    if mode == "Text":
        text = hashing_input.get()
        

        if not text:
            return
    
    
        
        result = hashlib.new(algorithm, text.encode()).hexdigest()


    elif mode == "File":
        filepath = hashing_input.get()
        try:
            with open(filepath, 'rb') as f:
                result = hashlib.new(algorithm, f.read()).hexdigest()

        except FileNotFoundError:
            result = "File not found"


    hashing_output.delete("1.0", "end")
    hashing_output.insert("1.0", result)







def on_scan_mode_change(value):
    if value == "Custom":
        scanner_range1.grid()
        scanner_range2.grid()

    else:
        scanner_range1.grid_remove()
        scanner_range2.grid_remove()




def run_scan_gui():

    host = scanner_input.get()
    mode = scan_mode.get()


    if not host:
        return
    

    scanner_output.delete("1.0", "end")


    def scan_thread():
        if mode == "Popular":
            ports = [21,22,23,25,53,80,110,143,443,445,3306,3389,8080]
        elif mode == "Full":
            ports = range(1,65536)
        elif mode == "Custom":
            try:
                port1 = int(scanner_range1.get())
                port2 = int(scanner_range2.get())
                ports = range(port1, port2 + 1)

            except ValueError:
                app.after(0, lambda: scanner_output.insert("end", "Invalid port range\n"))
                return
            
        for port in ports:
            is_open = scan_port(host, port)

            if is_open:
                app.after(0, lambda p = port: scanner_output.insert("end", f"port {p} is open\n"))
        app.after(0, lambda: scanner_output.insert("end", "Scan complete\n"))
            

    thread = threading.Thread(target=scan_thread)
    thread.daemon = True
    thread.start()



def run_whois():
    domain = whois_input.get()
    if not domain:
        return
    
    try:
        result = whois.whois(domain)

        date = result.creation_date
        if isinstance(date, list):
            date = date[0]

        exp_date = result.expiration_date
        if isinstance(exp_date, list):
             exp_date = exp_date[0]


        output=f"""Domain: {result.domain_name or 'N/A'}
    Registrar: {result.registrar or 'N/A'}
    Organisation: {result.org or 'N/A'}
    Country: {result.country or 'N/A'}
    Created: {date.strftime('%Y-%m-%d') if date else 'N/A'}
    Expires: {exp_date.strftime('%Y-%m-%d') if exp_date else 'N/A'}
    Name Servers: {', '.join(result.name_servers) if result.name_servers else 'N/A'}"""


        whois_output.delete("1.0", "end")
        whois_output.insert("1.0", output)

        
    except Exception:
        whois_output.delete("1.0", "end")
        whois_output.insert("1.0", "Error performing WHOIS lookup")




def run_dns():
    domain = dns_input.get()
    record_type = dns_type.get()

    if not domain:
        return
    
    dns_output.delete("1.0", "end")


    def dns_thread():

        types_to_check = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"] if record_type == 'All' else [record_type]


        for rtype in types_to_check:
            try:
                results = dns.resolver.resolve(domain, rtype)
                for result in results:
                    app.after(0, lambda r=result, t=rtype: dns_output.insert("end", f"{t}: {r.to_text()}\n"))

            except dns.resolver.NoAnswer:
                app.after(0, lambda t=rtype: dns_output.insert("end", f"{t}: No records found\n"))

            except dns.resolver.NXDOMAIN:
                app.after(0, lambda: dns_output.insert("end", "Domain does not exist\n"))
                break

    thread = threading.Thread(target=dns_thread)
    thread.daemon = True
    thread.start()




def run_vt():

    url = vt_input.get()

    if not url:
        return
    vt_output.delete('1.0', 'end')


    def vt_thread():
        try:
            headers = {'x-apikey': api_key}
            response = requests.post(
                'https://www.virustotal.com/api/v3/urls',
                headers=headers,
                data={'url':url}
            )

            if response.status_code != 200:
                app.after(0,lambda: vt_output.insert('end', f'Error: {response.json()["error"]["message"]}\n'))
                return
            
            analysis_id = response.json()['data']['id']

            app.after(0, lambda: vt_output.insert('end', 'Analysing...\n'))

            while True:
                result = requests.get(
                    f'https://www.virustotal.com/api/v3/analyses/{analysis_id}',
                    headers=headers
                )

                status = result.json()['data']['attributes']['status']
                if status == 'completed':
                    break
                time.sleep(2)

            stats = result.json()['data']['attributes']['stats']
            output = f"""Malicious: {stats['malicious']}
            Suspicious: {stats['suspicious']}
            Harmless: {stats['harmless']}
            Undetected: {stats['undetected']}"""

            app.after(0, lambda: vt_output.delete('1.0', 'end'))
            app.after(0, lambda: vt_output.insert('end', output))
                
        except Exception as e:
            app.after(0, lambda: vt_output.insert('end', f'Error: {str(e)}\n'))


    thread = threading.Thread(target=vt_thread)
    thread.daemon = True
    thread.start()





def run_phishing():
    url = phishing_input.get()

    if not url:
        return
    phishing_output.delete('1.0', 'end')

    def phishing_thread():
        try:
            domain = urlparse(url).netloc
            heuristic_warnings = heuristic_check(url)
            domain_warnings = domain_age_check(domain)
            redirect_warnings = redirect_check(url)
            vt_result = scan_url(url, api_key)
            
            risk, score, colour = calculate_risk(vt_result, heuristic_warnings, domain_warnings, redirect_warnings)

            all_warnings = heuristic_warnings + domain_warnings + redirect_warnings

            output = f'Risk Level: {risk} (Score: {score}/5\n\n)'

            if all_warnings:
                output +="Warnings:\n"

                for warning in all_warnings:
                    output += f" ! {warning}\n"

            else:
                output += "No warnings found"

            app.after(0, lambda: phishing_output.insert('end', output))
        except Exception as e:
            app.after(0,lambda:phishing_output.insert('end',f'Error: {str(e)}\n'))

    thread = threading.Thread(target=phishing_thread)
    thread.daemon = True
    thread.start()







app = tk.CTk()
app.title("Cyber Toolkit")
app.geometry("900x600")
tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")

sidebar = tk.CTkFrame(app, width=200)
sidebar.grid(row=0, column=0, sticky="nsew")
tk.CTkLabel(sidebar, text="Tools", font=("Arial", 16, "bold")).pack(pady=20)


main_panel = tk.CTkFrame(app)
main_panel.grid(row=0, column=1, sticky="nsew")

app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

hashing_frame = tk.CTkFrame(main_panel)
hash_mode = tk.CTkSegmentedButton(hashing_frame, values=["Text", "File"])
hash_mode.set("Text")
hash_mode.grid(row=1, column=0, pady=5, padx=20, sticky="w")
hashing_frame.grid(row=0, column=0, sticky="nsew")
hashing_label = tk.CTkLabel(hashing_frame, text="Enter the text or file path here.")
hashing_label.grid(row=0,column=1, sticky="w")
hashing_input = tk.CTkEntry(hashing_frame, width=400, placeholder_text="Enter text to hash...")
hashing_input.grid(row = 2, column = 1, sticky="w")
hashing_options = tk.CTkOptionMenu(hashing_frame, values = ["MD5", "SHA1", "SHA256"])
hashing_options.grid(row = 1, column = 1, sticky="w")
tk.CTkButton(hashing_frame, text="Hash", command=run_hash).grid(row=3, column=0, pady=10)
hashing_output = tk.CTkTextbox(hashing_frame)
hashing_output.grid(row=4, column = 1, sticky = "nsew")
hashing_frame.grid_columnconfigure(0, weight=1)



scanner_frame = tk.CTkFrame(main_panel)
scanner_frame.grid(row=0, column=0,  sticky = "nsew")
scan_mode = tk.CTkSegmentedButton(scanner_frame, values = ["Popular", "Full", "Custom"], command=on_scan_mode_change)
scan_mode.set("Popular")
scan_mode.grid(row = 2, column = 0, pady=5, padx = 20, sticky = "w")

scanner_label = tk.CTkLabel(scanner_frame, text="Enter the target IP Here")
scanner_label.grid(row = 0, column = 1, sticky = "w")



scanner_input = tk.CTkEntry(scanner_frame, width = 400, placeholder_text="Enter the IP Address you would like to scan")
scanner_input.grid(row = 1, column = 1, sticky = "w")


scanner_range1 = tk.CTkEntry(scanner_frame, placeholder_text="Start port")
scanner_range1.grid(row = 3, column = 1, sticky = "w")
scanner_range1.grid_remove()
scanner_range2 = tk.CTkEntry(scanner_frame, placeholder_text="End Port")
scanner_range2.grid(row = 3, column = 2, sticky = "w")
scanner_range2.grid_remove()

scanner_button = tk.CTkButton(scanner_frame, text="Run scan", command = run_scan_gui)
scanner_button.grid(row = 4, column = 1, sticky = "w" )


scanner_output = tk.CTkTextbox(scanner_frame)
scanner_output.grid(row = 5, column = 1, sticky = "w")




whois_frame = tk.CTkFrame(main_panel)
whois_frame.grid(row = 0, column = 0, sticky = "nsew")

whois_input = tk.CTkEntry(whois_frame, width=400, placeholder_text="Enter a domain...")
whois_input.grid(row = 1, column = 1, sticky = "w")

whois_button = tk.CTkButton(whois_frame, text="WHOIS Lookup",command = lambda: run_whois())
whois_button.grid(row = 2, column = 1, sticky = "w")

whois_output = tk.CTkTextbox(whois_frame)
whois_output.grid(row = 3, column = 1, sticky = "w")




dns_frame =tk.CTkFrame(main_panel)
dns_frame.grid(row = 0, column = 0, sticky = "nsew")


dns_label = tk.CTkLabel(dns_frame, text="Enter the domain here...")
dns_label.grid(row=0,column=1,sticky='w')


dns_input = tk.CTkEntry(dns_frame, width=400, placeholder_text="Enter a domain...")
dns_input.grid(row=1, column=1, sticky='w')


dns_type = tk.CTkSegmentedButton(dns_frame, values=["All", "A", "AAAA", "MX", "NS", "TXT", "CNAME"])
dns_type.grid(row = 2, column = 1, sticky = 'w')

dns_button = tk.CTkButton(dns_frame, text= "DNS Lookup", command = lambda: run_dns())
dns_button.grid(row = 3, column = 1, sticky = 'w')


dns_output = tk.CTkTextbox(dns_frame)
dns_output.grid(row = 4, column = 1, sticky = 'w')



vt_frame = tk.CTkFrame(main_panel)
vt_frame.grid(row = 0, column = 0, sticky = 'nsew')


vt_label = tk.CTkLabel(vt_frame, text="Enter a URL to test..")
vt_label.grid(row = 0, column = 1, sticky = 'nsew')


vt_input = tk.CTkEntry(vt_frame, width = 400, placeholder_text="Enter URL")
vt_input.grid(row = 1, column=1, sticky = 'nsew')

vt_button = tk.CTkButton(vt_frame, text="Test URL", command =lambda:run_vt())
vt_button.grid(row =2, column = 1, sticky = 'w' )

vt_output = tk.CTkTextbox(vt_frame)
vt_output.grid(row = 3, column = 1, sticky='w')



phishing_frame = tk.CTkFrame(main_panel)
phishing_frame.grid(row=0, column=0, sticky='nsew')

phishing_label = tk.CTkLabel(phishing_frame, text='Enter a URL...')
phishing_label.grid(row=0,column=1,sticky='w')

phishing_input = tk.CTkEntry(phishing_frame, placeholder_text="Enter a URL")
phishing_input.grid(row = 1, column =1, sticky = 'w')

phishing_button = tk.CTkButton(phishing_frame, text='Check for phishing', command=lambda:run_phishing())
phishing_button.grid(row =2, column =1, sticky = 'w')

phishing_output = tk.CTkTextbox(phishing_frame)
phishing_output.grid(row = 3, column=1,sticky='w')


tools = [
    "Passwords",
    "Port Scanner",
    "Hashing",
    "WHOIS",
    "DNS",
    "VirusTotal",
    "Phishing",
    "Log Parser"
]

tk.CTkButton(sidebar, text="Passwords", command=lambda: None).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="Port Scanner", command=lambda: show_frame(scanner_frame)).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="Hashing", command=lambda: show_frame(hashing_frame)).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="WHOIS", command=lambda: show_frame(whois_frame)).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="DNS", command=lambda: show_frame(dns_frame)).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="VirusTotal", command=lambda: show_frame(vt_frame)).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="Phishing", command=lambda: show_frame(phishing_frame)).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="Log Parser", command=lambda: None).pack(pady=5, padx=10, fill="x")



app.mainloop()