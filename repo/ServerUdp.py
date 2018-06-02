import argparse
import socket

parser = argparse.ArgumentParser(description='Ip and port')
parser.add_argument('-i', '--ip', help='The ip of the Server', required=False, default="0.0.0.0")
parser.add_argument('-p', '--port', help='The port of the server', required=False, default=5000)
args = vars(parser.parse_args())

# Here we define the UDP IP address as well as the port number that we have
# already defined in the client python script.
UDP_IP_ADDRESS = args['ip']
UDP_PORT_NO = int(args['port'])
# declare our serverSocket upon which
# we will be listening for UDP messages
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
count = 0
DATA = []
while True:
    data, addr = serverSock.recvfrom(1024)
    print "Message: " + str(count), data
    count = count + 1
    if count % 3 == 0:
        print "Now I want to Send it"
