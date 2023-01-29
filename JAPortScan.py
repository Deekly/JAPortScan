import socket

myHost = input('Host --> ')
myPort = int(input('Port --> '))


def portscan(host, port):


    scan = socket.socket()

    try:
        scan.connect((host, port))
    except socket.error:
        print("Port -- ", port, '-- [CLOSED]')
    else:
        print('Port -- ', port, '-- [OPEN]')

portscan(myHost, myPort)

file = open('log.txt', 'w')
file.writelines('Host was {0}\n'.format(myHost))
file.writelines('Port was {0}'.format(myPort))

file.close()

