import socket


target_host = "127.0.0.1"
target_port = 9000


# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
connect = client.connect((target_host, target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data
response = client.recv(4096)

print(response)

client.close()