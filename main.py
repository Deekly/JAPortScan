import socket

def portscan():
    host = input('Host --> ')
    port = int(input('Port --> '))

    scan = socket.socket()

    try:
        scan.connect((host, port))
    except socket.error:
        print("Port -- ", port, '-- [CLOSED]')
    else:
        print('Port -- ', port, '-- [OPEN]')

portscan()