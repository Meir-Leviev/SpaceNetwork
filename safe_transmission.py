# Here we will put the transmission funcs and exceptions to keep our main clean
from space_network_lib import *

class BrokenConnectionError(CommsError):
    pass
