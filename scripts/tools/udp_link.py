#!/usr/bin/env python
import socket
import struct


class UDPLink(object):
    def __init__(self, ip="BAXTERFLOWERS.local", port=5005):
        self.ip = ip
        self.port = port

    def _send_data(self, channel, data, string_pattern):
        str_pat = 'I'
        str_pat += string_pattern
        packer = struct.Struct(str_pat)
        sent_vect = [channel] + data
        packed_data = packer.pack(*sent_vect)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        sock.sendto(packed_data, (self.ip, self.port))

    def send_int(self, channel, int_value):
        self._send_data(channel, [int_value], 'I')

    def send_float_vector(self, channel, vect):
        self._send_data(channel, vect, ('f' * len(vect)))
