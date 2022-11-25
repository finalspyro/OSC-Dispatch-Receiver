import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server

def print_volume_handler(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))

def print_compute_handler(unused_addr, args, volume):
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/filter", print)
dispatcher.map("/volume", print_volume_handler, "Volume")
dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)

server = osc_server.ThreadingOSCUDPServer(
    ("127.0.0.1", 57130), dispatcher)
print("Serving on {}".format(server.server_address))
server.serve_forever()