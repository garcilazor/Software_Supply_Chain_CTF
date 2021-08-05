import socket

def Main():
    s = socket.socket()
    s.bind(('', 7234))
    print("Bound socket")

    s.listen(1)
    while True:
      c, addr = s.accept()
      print("Got connection")
      data = c.recv(1024)
      data = str(data.decode())
      print("Got data: " + data)
      c.close()

if __name__ == '__main__':
    Main()

