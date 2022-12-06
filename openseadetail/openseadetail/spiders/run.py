import subprocess
import os

homeDir = os.system('cd ~')
print('cd ~ run with exit code : %d'%homeDir)

print('')

list_files = subprocess.run(['ls', '-l'])
# print('the exit code was %d'%list_files)
