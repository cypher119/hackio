import subprocess
import time
import sys
import random

t = int(sys.argv[1])
s = random.randint(30, 60)

for i in range(t):
    subprocess.run(['xdotool', 'key', 'Ctrl+Tab'])
    time.sleep(s)
    
