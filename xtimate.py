import subprocess
import time
import sys

t = int(sys.argv[1])

for i in range(t):
    subprocess.run(['xdotool', 'key', 'Alt+Tab'])
    time.sleep(40)
