from space_network_lib import *
import time
from safe_transmission import BrokenConnectionError, RelayPacket

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

ship1 = SpaceNetwork(level=4)
sat1 = Satellite("sat1", 100)
sat2 = Satellite("sat2", 200)
msg = Packet("Hello from sat1!", sat1, sat2)

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
    attempt_transmission(msg)
except BrokenConnectionError:
    print("Transmission failed")