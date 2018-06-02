import argparse
import socket


def send_udp(ip, port, message):
    udp_ip_address = ip
    udp_port_no = port
    Message = message
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSock.sendto(Message, (udp_ip_address, udp_port_no))


def buffer_manipulation():
    print "manipulate"
    # TODO: add you manipulation logic


def main():
    parser = argparse.ArgumentParser(description='Ip and port')
    parser.add_argument('-i', '--ip', help='The ip of the Server', required=False, default="0.0.0.0")
    parser.add_argument('-p', '--port', help='The port of the server', required=False, default=5001)
    parser.add_argument('--phone_ip', help='The ip of the Server', required=False, default="0.0.0.0")
    parser.add_argument('--phone_port', help='The port of the server', required=False, default=5002)
    parser.add_argument('--debug', action='store_true', help='for Data and count play')
    args = vars(parser.parse_args())
    udp_ip_address = args['ip']
    udp_port_no = int(args['port'])
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((udp_ip_address, udp_port_no))
    count = 0
    dlist = []

    while True:

        data, addr = server_socket.recvfrom(1024)
        print "Message: " + str(count), data
        count = count + 1
        dlist.append(data + ": " + str(count))
        if count % 3 == 0:
            print "Now I want to Send it"
            udpBuffer = dlist[:-4:-1]
            for i in udpBuffer:
                send_udp(ip=args['phone_ip'], port=int(args['phone_port']), message=i)
            udpBuffer[:] = []


if __name__ == '__main__':
    main()
