# Here we will put the transmission funcs and exceptions to keep our main clean
from space_network_lib import *

class BrokenConnectionError(CommsError):
    pass

class RelayPacket(Packet):
    def __init__(self, packet_to_relay, sender, proxy):
        super().__init__(data=packet_to_relay, sender=sender, receiver=proxy)

    def __repr__(self):
        return f"RelayPacket(Relaying [{self.data}] to {self.receiver}from {self.sender})"

def wrap_r_p(p_final, lst_sat):
    r_pac = p_final
    for i in range(len(lst_sat) -2, 0,-1):
        r_pac = RelayPacket(r_pac , lst_sat[i-1], lst_sat[i])
    return r_pac