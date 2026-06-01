import customtkinter as tk
import hashlib

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
tk.CTkButton(sidebar, text="Port Scanner", command=lambda: None).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="Hashing", command=lambda: show_frame(hashing_frame)).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="WHOIS", command=lambda: None).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="DNS", command=lambda: None).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="VirusTotal", command=lambda: None).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="Phishing", command=lambda: None).pack(pady=5, padx=10, fill="x")
tk.CTkButton(sidebar, text="Log Parser", command=lambda: None).pack(pady=5, padx=10, fill="x")



app.mainloop()