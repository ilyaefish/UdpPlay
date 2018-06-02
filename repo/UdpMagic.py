import argparse
import socket
import time


def buffer_manipulation(buffer_list, manipulation_type):
    if manipulation_type == "reverse":

        reverse_list = buffer_list[::-1]
        return reverse_list
    elif manipulation_type == "duplicate":
        duplicate_list = []
        for i in buffer_list:
            duplicate_list.append(i)
            duplicate_list.append(i)
        return duplicate_list
    elif manipulation_type == "double":
        double_list = buffer_list[:]
        double_list.extend(buffer_list)
        return double_list


class UdpMagic:
    server_socket = None
    udp_buffer = []  # type: List[Any]

    def __init__(self, ip, port, phone_ip, phone_port):
        self.ip = ip
        self.port = port
        self.phone_ip = phone_ip
        self.phone_port = phone_port

    def server_up(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.ip, self.port))

    def send_udp(self, data):
        message = data
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_sock.sendto(message, (self.phone_ip, self.phone_port))


def main():
    parser = argparse.ArgumentParser(description='Ip and port')
    parser.add_argument('-i', '--ip', help='The ip of the Server', required=False, default="0.0.0.0")
    parser.add_argument('-p', '--port', help='The port of the server', required=False, default=5001)
    parser.add_argument('--phone_ip', help='The ip of the Server', required=False, default="192.168.1.1")
    parser.add_argument('--manipulation_type', help='The manipulation type; reverse, duplicate, double', required=False,
                        default="reverse")
    parser.add_argument('--phone_port', help='The port of the server', required=False, default=5002)
    parser.add_argument('--bsize', help='Buffer Size, The number of the udp packet you want to buffer ', required=False,
                        default=3)
    parser.add_argument('--client', action='store_true', help='When you run the service as a client', required=False)
    parser.add_argument('--debug', action='store_true', help='Debugger', required=False)
    args = vars(parser.parse_args())
    print "Running server with"
    print args
    magic = UdpMagic(ip=args['ip'], port=int(args['port']), phone_ip=args['phone_ip'],
                     phone_port=int(args['phone_port']))
    if args['client']:
        ts = time.time()
        magic.send_udp(str(ts))
        if args["debug"]:
            print ts

    else:
        magic.server_up()
        count = 0
        magic.udp_buffer = []
        # received_data = []

        while True:
            data, addr = magic.server_socket.recvfrom(1024)
            print "Message: " + str(count), data
            count = count + 1
            magic.udp_buffer.append(data + ": " + str(count))
            if count % int(args["bsize"]) == 0:
                udp_buffer = buffer_manipulation(magic.udp_buffer.append, manipulation_type=args['manipulation_type'])
                for i in udp_buffer:
                    magic.send_udp(data=i)
                magic.udp_buffer[:] = []
                # received_data[:] = []


if __name__ == '__main__':
    main()
