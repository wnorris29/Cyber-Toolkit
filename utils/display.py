import os 

from rich.console import Console

console = Console()

def clear():
    os.system('cls' if os.name =='nt' else 'clear')

