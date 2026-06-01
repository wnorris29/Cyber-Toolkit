import customtkinter as tk
import hashlib
import threading
from tools.port_scanner import scan_port

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
tk.CTkButton(sidebar, text="WHOIS", command=lambda: None).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="DNS", command=lambda: None).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="VirusTotal", command=lambda: None).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="Phishing", command=lambda: None).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="Log Parser", command=lambda: None).pack(pady=5, padx=10, fill="x")



app.mainloop()