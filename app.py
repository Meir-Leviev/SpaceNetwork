from space_network_lib import *

class Satellite(SpaceEntity):

    def receive_signal(self, packet: Packet):
        print( f"[{self.name}] Received: {packet}" )

ship1 = SpaceNetwork(level=1)
sat1 = Satellite("sat1", 100)
sat2 = Satellite("sat2", 200)
msg = Packet("Hello from sat1!", sat1, sat2)

ship1.send(msg)