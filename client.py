import socket

def inity():
    
    print('initialization of the client...')
    sock = socket.socket()
    sock.setblocking(1)

    print('do you wanna enter IP-address? [yes/no]')
    yn = input()
    if yn == 'yes':
        print('enter the IP address: ')
        ad = str(input())
    elif yn == 'no':
        ad = 'localhost'
    else:
        print('youre an idiot')
    
    print('do you wanna enter port №? [yes/no]')
    yn = input()
    if yn == 'yes':
        print('enter the port №: ')
        pt = int(input())
    elif yn == 'no':
        pt = 9090
    else:
        print('youre an idiot')
    print('connecting to {} {}...'.format(ad, pt))
    
    sock.connect((ad, pt))
    
    return sock

sock = inity()

data = sock.recv(1024)
print(data.decode())
if data.decode()[0] == 'p':
    msg = input()
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(data.decode())

while True:
#    print('я вошел в цикл')
    print('enter your message: ')
    msg = input()
    try: 
        sock.send(msg.encode())
        data = sock.recv(1024)
        print(data.decode())    
    except ConnectionResetError or ConnectionAbortedError:
        print('The server didnt answer.')
        break
    if msg == 'exit' or msg == 'serverdie':
        break

sock.close()

print(data.decode())



"""
проверка ввода в отдельную функцию (?),
автоматическое изменение порта
"""