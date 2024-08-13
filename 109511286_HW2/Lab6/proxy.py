#!/usr/bin/env python3

import socket
import ssl
import threading

def process_request(ssock_for_browser):
    hostname = 'codeforces.com'
    port = 443
    cadir = '/etc/ssl/certs'
    #cadir = './client-certs'
    
    sock_for_server = socket.create_connection((hostname, port))
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(capath=cadir)
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    print("sock_for_server")
    
    #sock_for_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock_for_server.connect((hostname, port))

    ssock_for_server = context.wrap_socket(sock_for_server, server_hostname=hostname, do_handshake_on_connect=False)
    ssock_for_server.do_handshake()
        
    request = ssock_for_browser.recv(2048)
    
    if request:
        ssock_for_server.sendall(request)
        
        response = ssock_for_server.recv(2048)
        while response:
            ssock_for_browser.sendall(response)
            response = ssock_for_server.recv(2048)
    
    ssock_for_server.close()

    ssock_for_browser.shutdown(socket.SHUT_RDWR)
    ssock_for_browser.close()

SERVER_CERT = './cf.crt'
SERVER_PRIVATE = './cf.key'

context_srv = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context_srv.load_cert_chain(SERVER_CERT, SERVER_PRIVATE)

sock_listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock_listen.bind(('0.0.0.0', 443))
sock_listen.listen(5)

print("listening")

while True:
    sock_for_browser, fromaddr = sock_listen.accept()
    print(f"Connection accepted from {fromaddr}")
    ssock_for_browser = context_srv.wrap_socket(sock_for_browser, server_side=True)
    x = threading.Thread(target=process_request, args=(ssock_for_browser,))
    x.start()
