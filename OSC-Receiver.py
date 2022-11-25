from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client
from typing import List, Any


def main(address: str, *osc_arguments):
    msg = osc_arguments[0]
    print(osc_arguments[0])

def sc_receiver(ip,port,path):
    disp = dispatcher.Dispatcher()
    handler = disp.map(path, main)
    server = osc_server.ThreadingOSCUDPServer((ip,port), disp)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()

if __name__ == '__main__':
    sc_receiver("127.0.0.1", 57130, "/filter")