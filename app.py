from space_network_lib import *
import time
from safe_transmission import BrokenConnectionError, RelayPacket, wrap_r_p, smart_send_packet

class Satellite(SpaceEntity):

    def receive_signal(self, packet: Packet):
        if isinstance(packet, RelayPacket):
            inner_packet = packet.data
            print(f"[{self.name}] Unwrapping and forwarding to {inner_packet.receiver}")
            attempt_transmission(inner_packet)
        else:
            print(f"[{self.name}] Final destination reached: {packet.data}")

class Earth(SpaceEntity):

    def receive_signal(self, packet: Packet):
        pass

ship1 = SpaceNetwork(level=1)
earth = Earth("Earth",0)
sat1 = Satellite("sat1", 50)
sat2 = Satellite("sat2", 100)
sat3 = Satellite("sat3", 150)
sat4 = Satellite("sat4", 200)
sat5 = Satellite("sat5", 250)
sat6 = Satellite("sat6", 300)
l_sat = [earth,sat1,sat2,sat3,sat4, sat5]
# msg = Packet("Hello from sat1!", sat1, sat2)
msg1 = Packet("Hello from Earth!", earth, sat6)
packet1 = smart_send_packet(msg1, l_sat)


def attempt_transmission(packet):
    while True:
        try:
            ship1.send(packet)
            break

        except TemporalInterferenceError:
            print("Interference, waiting...")
            time.sleep(2)

        except DataCorruptedError:
            print("Data corrupted, retrying...")

        except LinkTerminatedError:
            print("Link lost")
            raise BrokenConnectionError

        except OutOfRangeError:
            print("Target out of range")
            raise BrokenConnectionError


try:
    attempt_transmission(packet1)
except BrokenConnectionError:
    print("Transmission failed")


