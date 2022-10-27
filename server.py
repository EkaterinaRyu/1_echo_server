import socket

from time import sleep

import logging

def logg(text):
    logger = logging.getLogger()
    handler = logging.FileHandler('logfile.log')
    logger.addHandler(handler)
    logger.error(text)


def connection_to_client():

    connected = False
    while not connected:
        try:
            sock = socket.socket()
            sock.bind(('', 9090))
            sock.listen(1)
            conn, addr = sock.accept()
            logg('initialization of the server...')
            logg('connection established: {}'.format(addr))
            connected = True
        except:
            sock.close()
            sleep(10)
    return conn, addr
                        
def log_check(conn, addr):
    t = False
    ipe, sk = addr
    with open(r'E:\Финашка\Алгоритмы\эхо-сервер\1_echo_server_002\loginsIPs.txt', 'r') as f:
        for i in f.readlines():
            i = i.split(':')
            if i[0] == ipe:
                conn.send('oh, i know you, {}'. format(i[1]).encode())
                t = True
        if t == False:
            conn.send('please, enter your login:'.encode())
            log = conn.recv(1024).decode()
            print(log)
            with open(r'E:\Финашка\Алгоритмы\эхо-сервер\1_echo_server_002\loginsIPs.txt', 'a+') as f:
                f.write(ipe + ':' + log + '\n')
            conn.send('hello, {}'.format(log).encode())
       
def main():
    conn, addr = connection_to_client()
    log_check(conn, addr)
    while True:
        data = conn.recv(1024)
        if not data:
            logg('no data recieved, closing the connection...')
            break
        msg = data.decode()
        if msg == 'exit':
            logg('closing the connection...')
            conn.close()
            conn, addr = connection_to_client()
            log_check(conn, addr)
            sleep(10)
        elif msg == 'serverdie':
            conn.close()
            logg('killing the server...')
            break
        conn.send(data)
        print(msg)
        
    
main()