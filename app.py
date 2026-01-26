from space_network_lib import *

class Satellite(SpaceEntity):

    def receive_signal(self, packet: Packet):
        print( f"[{self.name}] Received: {packet}" )