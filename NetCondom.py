import socket

ip = raw_input("IP: ")
port = int(raw_input("Port: "))

try:
    s = socket.socket()
    s.settimeout(5)
    s.connect((ip,port))
    s.send("HEAD / HTTP/1.0 \r\n\r\n")
    
    result = s.recv(1024)
    s.close()
    print str(result)

except Exception, e:
    print str (e) 
    import socket