import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 5508)
sock.connect(addr)
for x in range(10):
    outMsg = "Message " + str(x)
    try:
        sock.sendall(outMsg.encode())
        print("Sent message: " + outMsg)
        returnMsg = sock.recv(1024).decode()
        print("Got back: " + returnMsg)
    except:
        #print("Something bad happened")
        sock.close()
        
