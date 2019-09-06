import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("0.0.0.0", 5508)
sock.bind(addr)
sock.listen(5)
while(True):
    (connectedSock, clientAddress) = sock.accept()
    try:
        while(True):
            msg = connectedSock.recv(1024).decode()
            print("Got message " + msg)
            returnMsg = "Here's the stuff: " + msg
            print("Returning message " + returnMsg)
            connectedSock.sendall(returnMsg.encode())
    except:
        print("Connection is closing")
        connectedSock.close()
        
