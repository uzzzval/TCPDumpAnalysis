import subprocess

from subprocess import Popen, PIPE

sudo_password = 'PASSWORD'
command = 'tcpdump port 443'.split()

p = Popen(['sudo', '-S'] + command, stdin=PIPE, stderr=PIPE,
          universal_newlines=True)
sudo_prompt = p.communicate(sudo_password + '\n')[1]
print sudo_prompt
