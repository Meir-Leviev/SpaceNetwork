from space_network_lib import *
import time
from safe_transmission import BrokenConnectionError

class Satellite(SpaceEntity):

    def receive_signal(self, packet: Packet):
        print( f"[{self.name}] Received: {packet}" )

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