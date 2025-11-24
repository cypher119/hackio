import subprocess
import time
import sys

t = int(sys.argv[1])
s = int(sys.argv[2])

for i in range(t):
    subprocess.run(['xdotool', 'key', 'Ctrl+Tab'])
    time.sleep(s)
