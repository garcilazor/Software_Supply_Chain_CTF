import socket

def Main():
    host = '172.23.231.117'

    port = 42424
    s = socket.socket()
    s.bind((host, port))
    print("Bound socket")

    s.listen(1)
    while True:
      c, addr = s.accept()
      print("Got connection")
      data = c.recv(1024)
      data = str(data.decode())
      print("Got a password: " + data)
      c.close()

if __name__ == '__main__':
    Main()

