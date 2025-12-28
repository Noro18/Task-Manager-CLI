import json
from pathlib import Path

DATA_FILE = Path("data/tasks.json")

def load_tasks():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, 'r') as f: # with keyword ne hanesan replacement dt ba try catch exeption iha python tanba nia automatically taka file nia jadi no memory leaks 
        return json.load(f)
    
def save_tasks(tasks):
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w") as f: # wainhira run uza 'w' mak nia file sira sei truncated ou terhapus 
        json.dump(tasks, f, indent=2)
