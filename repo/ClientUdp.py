import argparse
import socket

parser = argparse.ArgumentParser(description='Ip and port')
parser.add_argument('-i', '--ip', help='The ip of the Server', required=False, default="127.0.0.1")
parser.add_argument('-p', '--port', help='The port of the server', required=False, default=5000)
args = vars(parser.parse_args())

UDP_IP_ADDRESS = args['ip']
UDP_PORT_NO = int(args['port'])
Message = "Hello, Server"
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
