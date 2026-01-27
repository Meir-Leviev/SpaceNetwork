# Here we will put the transmission funcs and exceptions to keep our main clean
from space_network_lib import *

class BrokenConnectionError(CommsError):
    pass

class RelayPacket(Packet):
    def __init__(self, packet_to_relay, sender, proxy):
        super().__init__(data=packet_to_relay, sender=sender, receiver=proxy)

    def __repr__(self):
        return f"RelayPacket(Relaying [{self.data}] to {self.receiver}from {self.sender})"

def wrap_r_p(p_final, lst):
    lst_sat = lst[::-1]
    r_pac = p_final
    for i in range(len(lst_sat) -2, 0,-1):
        r_pac = RelayPacket(r_pac , lst_sat[i-1], lst_sat[i])
    return r_pac

def smart_send_packet(packet, lst_sat: list):
    sender = packet.sender
    receiver = packet.receiver
    new_lst = [receiver]
    temp_receiver = receiver
    i = lst_sat.index(sender)
    while temp_receiver != sender:
        if lst_sat[i].distance_from_earth + 150 >= temp_receiver.distance_from_earth:
            new_lst.append(lst_sat[i])
            temp_receiver = lst_sat[i]
            i = lst_sat.index(sender)
        else:
            i += 1
    return wrap_r_p(packet, new_lst)