import subprocess
import sys

print(sys.platform)

cmd = ['ping', '127.0.0.1']

proc = subprocess.run(cmd, encoding='utf-8')

print(proc)
print(proc.stdout)
print(proc.stderr)