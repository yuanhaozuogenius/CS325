import subprocess
import time
import sys
import os

def main(arr):
    startTime = time.time()
    process = subprocess.Popen(arr)
    process.wait()
    print("running time: ", time.time() - startTime)

main(["python"] + sys.argv[1:])

# usage:
#   python timing.py <program> <arguments>
#   e.g
#   python timing.py primes.py

